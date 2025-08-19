"""Enhanced douga command for AI-powered video frame interpolation."""

import json
import sys
from pathlib import Path
from typing import List, Optional, Union

from .config import DougaConfig, VideoProcessingConfig
from .processor import VideoProcessor


def douga(
    videos: Union[str, List[str]],
    config: Optional[str] = None,
    output_dir: Optional[str] = None,
    target_fps: float = 60.0,
    quality: str = "high",
    interpolation_factor: Optional[float] = None,
    output_format: str = "mp4",
    batch_size: int = 1,
    dry_run: bool = False,
    verbose: bool = False,
    force_overwrite: bool = False,
    preserve_audio: bool = True,
    use_gpu: bool = True,
    resolution_scale: float = 1.0,
    temp_dir: Optional[str] = None
):
    """
    AI-powered video frame interpolation using Saibyo.
    
    Processes one or more video files to increase their framerate using deep learning
    frame interpolation techniques.
    
    Args:
        videos: Single video file path or list of video file paths to process
        config: Path to configuration file (JSON, YAML, or TOML)
        output_dir: Directory to save processed videos (default: same as input)
        target_fps: Target output framerate (default: 60.0)
        quality: Processing quality level: low, medium, high, ultra (default: high)
        interpolation_factor: Manual interpolation multiplier (overrides target_fps)
        output_format: Output video format: mp4, avi, mkv, mov (default: mp4)
        batch_size: Number of videos to process simultaneously (default: 1)
        dry_run: Preview operations without executing (default: False)
        verbose: Enable detailed logging (default: False)
        force_overwrite: Overwrite existing output files (default: False)
        preserve_audio: Keep original audio track (default: True)
        use_gpu: Use GPU acceleration if available (default: True)
        resolution_scale: Scale resolution by factor (default: 1.0)
        temp_dir: Temporary directory for processing files
    
    Examples:
        # Process single video
        douga("video.mp4")
        
        # Process multiple videos with custom settings
        douga(["video1.mp4", "video2.mp4"], target_fps=120, quality="ultra")
        
        # Use configuration file
        douga("video.mp4", config="config.json")
        
        # Dry run to preview operations
        douga(["*.mp4"], dry_run=True, verbose=True)
    """
    try:
        # Create processing configuration
        processing_config = VideoProcessingConfig(
            target_fps=target_fps,
            interpolation_factor=interpolation_factor,
            quality=quality,
            resolution_scale=resolution_scale,
            output_format=output_format,
            output_directory=Path(output_dir) if output_dir else None,
            preserve_audio=preserve_audio,
            batch_size=batch_size,
            use_gpu=use_gpu,
            temp_directory=Path(temp_dir) if temp_dir else None
        )
        
        # Handle video paths (support glob patterns)
        video_paths = _resolve_video_paths(videos)
        
        # Create main configuration
        douga_config = DougaConfig(
            video_paths=video_paths,
            config_file=Path(config) if config else None,
            processing=processing_config,
            dry_run=dry_run,
            verbose=verbose,
            force_overwrite=force_overwrite
        )
        
        # Load configuration file if provided
        if config:
            douga_config = _load_config_file(douga_config, Path(config))
        
        # Display configuration summary
        _display_config_summary(douga_config)
        
        # Process videos
        processor = VideoProcessor(douga_config)
        success = processor.process_videos()
        
        if success:
            print(f"\n🎉 Successfully processed {len(video_paths)} video(s)!")
            return 0
        else:
            print(f"\n❌ Some videos failed to process. Check logs for details.")
            return 1
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        if verbose:
            import traceback
            traceback.print_exc()
        return 1


def _resolve_video_paths(videos: Union[str, List[str]]) -> List[Path]:
    """Resolve video file paths, including glob patterns."""
    import glob
    
    if isinstance(videos, str):
        videos = [videos]
    
    resolved_paths = []
    for video_pattern in videos:
        # Handle glob patterns
        if '*' in video_pattern or '?' in video_pattern:
            matches = glob.glob(video_pattern)
            resolved_paths.extend([Path(match) for match in sorted(matches)])
        else:
            resolved_paths.append(Path(video_pattern))
    
    # Remove duplicates while preserving order
    unique_paths = []
    seen = set()
    for path in resolved_paths:
        if path not in seen:
            unique_paths.append(path)
            seen.add(path)
    
    return unique_paths


def _load_config_file(config: DougaConfig, config_path: Path) -> DougaConfig:
    """Load configuration from file and merge with existing config."""
    print(f"📄 Loading configuration from: {config_path}")
    
    try:
        if config_path.suffix.lower() == '.json':
            with open(config_path, 'r') as f:
                file_config = json.load(f)
        elif config_path.suffix.lower() in ['.yaml', '.yml']:
            import yaml
            with open(config_path, 'r') as f:
                file_config = yaml.safe_load(f)
        elif config_path.suffix.lower() == '.toml':
            import tomllib
            with open(config_path, 'rb') as f:
                file_config = tomllib.load(f)
        else:
            raise ValueError(f"Unsupported configuration format: {config_path.suffix}")
        
        # Merge file configuration with existing configuration
        # For now, just update the processing config with file values
        if 'processing' in file_config:
            for key, value in file_config['processing'].items():
                if hasattr(config.processing, key):
                    setattr(config.processing, key, value)
        
        return config
        
    except ImportError as e:
        print(f"❌ Missing dependency for config format {config_path.suffix}: {e}")
        print("Install with: pip install pyyaml (for YAML) or use JSON format")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error loading configuration file: {e}")
        sys.exit(1)


def _display_config_summary(config: DougaConfig):
    """Display configuration summary."""
    print(f"\n🎬 Douga - AI Video Frame Interpolation")
    print(f"{'='*50}")
    
    print(f"📹 Input videos: {len(config.video_paths)}")
    for i, path in enumerate(config.video_paths[:5], 1):  # Show first 5
        print(f"  {i}. {path.name}")
    if len(config.video_paths) > 5:
        print(f"  ... and {len(config.video_paths) - 5} more")
    
    print(f"\n⚙️  Processing settings:")
    print(f"  Target FPS: {config.processing.target_fps}")
    print(f"  Quality: {config.processing.quality}")
    print(f"  Output format: {config.processing.output_format}")
    print(f"  Resolution scale: {config.processing.resolution_scale}x")
    print(f"  GPU acceleration: {'✓' if config.processing.use_gpu else '✗'}")
    print(f"  Preserve audio: {'✓' if config.processing.preserve_audio else '✗'}")
    
    if config.processing.output_directory:
        print(f"  Output directory: {config.processing.output_directory}")
    
    if config.dry_run:
        print(f"\n🔍 DRY RUN MODE - No files will be modified")
    
    print(f"{'='*50}")
