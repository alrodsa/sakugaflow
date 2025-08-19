"""Configuration models for the douga command."""

import os
from pathlib import Path
from typing import List, Optional, Union
from pydantic import BaseModel, Field, validator


class VideoProcessingConfig(BaseModel):
    """Configuration for video processing parameters."""
    
    # Frame interpolation settings
    target_fps: float = Field(default=60.0, ge=24.0, le=240.0, description="Target output framerate")
    interpolation_factor: Optional[float] = Field(default=None, ge=1.0, le=10.0, description="Interpolation multiplier")
    
    # Quality settings
    quality: str = Field(default="high", description="Processing quality level")
    resolution_scale: float = Field(default=1.0, ge=0.1, le=4.0, description="Resolution scaling factor")
    
    # Processing options
    output_format: str = Field(default="mp4", description="Output video format")
    output_directory: Optional[Path] = Field(default=None, description="Output directory for processed videos")
    preserve_audio: bool = Field(default=True, description="Whether to preserve original audio")
    
    # Advanced settings
    batch_size: int = Field(default=1, ge=1, le=8, description="Number of videos to process simultaneously")
    use_gpu: bool = Field(default=True, description="Whether to use GPU acceleration")
    temp_directory: Optional[Path] = Field(default=None, description="Temporary directory for processing")
    
    @validator('quality')
    def validate_quality(cls, v):
        """Validate quality setting."""
        allowed_qualities = ['low', 'medium', 'high', 'ultra']
        if v not in allowed_qualities:
            raise ValueError(f"Quality must be one of {allowed_qualities}")
        return v
    
    @validator('output_format')
    def validate_output_format(cls, v):
        """Validate output format."""
        allowed_formats = ['mp4', 'avi', 'mkv', 'mov']
        if v not in allowed_formats:
            raise ValueError(f"Output format must be one of {allowed_formats}")
        return v
    
    @validator('output_directory', 'temp_directory', pre=True, always=True)
    def validate_directories(cls, v):
        """Validate and create directories if needed."""
        if v is None:
            return v
        
        path = Path(v)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        
        if not path.is_dir():
            raise ValueError(f"Path {v} is not a directory")
        
        return path


class DougaConfig(BaseModel):
    """Main configuration for the douga command."""
    
    # Input settings
    video_paths: List[Path] = Field(description="List of input video file paths")
    config_file: Optional[Path] = Field(default=None, description="Path to configuration file")
    
    # Processing configuration
    processing: VideoProcessingConfig = Field(default_factory=VideoProcessingConfig)
    
    # Execution settings
    dry_run: bool = Field(default=False, description="Preview operations without executing")
    verbose: bool = Field(default=False, description="Enable verbose logging")
    force_overwrite: bool = Field(default=False, description="Overwrite existing output files")
    
    @validator('video_paths', pre=True)
    def validate_video_paths(cls, v):
        """Validate video file paths."""
        if isinstance(v, (str, Path)):
            v = [v]
        
        validated_paths = []
        for path in v:
            path = Path(path)
            if not path.exists():
                raise ValueError(f"Video file not found: {path}")
            if not path.is_file():
                raise ValueError(f"Path is not a file: {path}")
            if path.suffix.lower() not in ['.mp4', '.avi', '.mkv', '.mov', '.webm']:
                raise ValueError(f"Unsupported video format: {path.suffix}")
            validated_paths.append(path)
        
        return validated_paths
    
    @validator('config_file', pre=True)
    def validate_config_file(cls, v):
        """Validate configuration file."""
        if v is None:
            return v
        
        path = Path(v)
        if not path.exists():
            raise ValueError(f"Configuration file not found: {path}")
        if not path.is_file():
            raise ValueError(f"Configuration path is not a file: {path}")
        if path.suffix.lower() not in ['.json', '.yaml', '.yml', '.toml']:
            raise ValueError(f"Unsupported configuration format: {path.suffix}")
        
        return path

    def get_output_path(self, input_path: Path) -> Path:
        """Generate output path for a given input video."""
        output_dir = self.processing.output_directory or input_path.parent
        output_name = f"{input_path.stem}_interpolated.{self.processing.output_format}"
        return output_dir / output_name