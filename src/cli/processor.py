"""Video processing utilities for the douga command."""

import json
import logging
import time
from pathlib import Path
from typing import List, Optional

from .config import DougaConfig, VideoProcessingConfig


class VideoProcessor:
    """Handles video processing operations for frame interpolation."""
    
    def __init__(self, config: DougaConfig):
        self.config = config
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        """Setup logging configuration."""
        logger = logging.getLogger("douga.processor")
        
        # Clear any existing handlers
        logger.handlers.clear()
        
        # Set level based on verbose flag
        level = logging.DEBUG if self.config.verbose else logging.INFO
        logger.setLevel(level)
        
        # Create console handler
        handler = logging.StreamHandler()
        handler.setLevel(level)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        return logger
    
    def process_videos(self) -> bool:
        """Process all videos according to configuration."""
        self.logger.info(f"Starting batch processing of {len(self.config.video_paths)} video(s)")
        
        if self.config.dry_run:
            self.logger.info("DRY RUN MODE - No actual processing will be performed")
            return self._dry_run_preview()
        
        success_count = 0
        total_videos = len(self.config.video_paths)
        
        for i, video_path in enumerate(self.config.video_paths, 1):
            self.logger.info(f"Processing video {i}/{total_videos}: {video_path.name}")
            
            try:
                success = self._process_single_video(video_path)
                if success:
                    success_count += 1
                    self.logger.info(f"✓ Successfully processed: {video_path.name}")
                else:
                    self.logger.error(f"✗ Failed to process: {video_path.name}")
            
            except Exception as e:
                self.logger.error(f"✗ Error processing {video_path.name}: {str(e)}")
                if self.config.verbose:
                    self.logger.exception("Full error details:")
        
        self.logger.info(f"Batch processing complete: {success_count}/{total_videos} videos processed successfully")
        return success_count == total_videos
    
    def _process_single_video(self, video_path: Path) -> bool:
        """Process a single video file."""
        output_path = self.config.get_output_path(video_path)
        
        # Check if output already exists
        if output_path.exists() and not self.config.force_overwrite:
            self.logger.warning(f"Output file already exists: {output_path}")
            self.logger.warning("Use --force-overwrite to overwrite existing files")
            return False
        
        # Get video info
        video_info = self._get_video_info(video_path)
        self.logger.debug(f"Video info: {video_info}")
        
        # Calculate interpolation parameters
        interpolation_params = self._calculate_interpolation_params(video_info)
        self.logger.debug(f"Interpolation params: {interpolation_params}")
        
        # Simulate processing (placeholder for actual Saibyo integration)
        self.logger.info(f"Interpolating frames: {video_info['fps']:.2f} fps → {self.config.processing.target_fps:.2f} fps")
        
        # Simulate processing time
        processing_time = self._simulate_processing(video_info)
        
        # Create output file info
        output_info = {
            "input_file": str(video_path),
            "output_file": str(output_path),
            "original_fps": video_info['fps'],
            "target_fps": self.config.processing.target_fps,
            "interpolation_factor": interpolation_params['factor'],
            "processing_time": processing_time,
            "quality": self.config.processing.quality,
            "resolution_scale": self.config.processing.resolution_scale
        }
        
        # Save processing info
        info_path = output_path.with_suffix('.json')
        with open(info_path, 'w') as f:
            json.dump(output_info, f, indent=2)
        
        self.logger.info(f"Output saved to: {output_path}")
        self.logger.info(f"Processing info saved to: {info_path}")
        
        return True
    
    def _get_video_info(self, video_path: Path) -> dict:
        """Get video file information."""
        # Placeholder implementation - in real implementation, would use ffprobe or opencv
        return {
            "path": str(video_path),
            "duration": 120.5,  # seconds
            "fps": 24.0,
            "width": 1920,
            "height": 1080,
            "format": video_path.suffix[1:],
            "size_mb": video_path.stat().st_size / (1024 * 1024) if video_path.exists() else 0
        }
    
    def _calculate_interpolation_params(self, video_info: dict) -> dict:
        """Calculate interpolation parameters."""
        original_fps = video_info['fps']
        target_fps = self.config.processing.target_fps
        
        # Calculate interpolation factor
        if self.config.processing.interpolation_factor:
            factor = self.config.processing.interpolation_factor
            calculated_fps = original_fps * factor
        else:
            factor = target_fps / original_fps
            calculated_fps = target_fps
        
        return {
            "factor": factor,
            "original_fps": original_fps,
            "calculated_fps": calculated_fps,
            "frame_count_original": int(video_info['duration'] * original_fps),
            "frame_count_interpolated": int(video_info['duration'] * calculated_fps)
        }
    
    def _simulate_processing(self, video_info: dict) -> float:
        """Simulate video processing with realistic timing."""
        # Simulate processing time based on video size and quality
        base_time = video_info['size_mb'] * 0.1  # Base time per MB
        
        quality_multipliers = {
            'low': 0.5,
            'medium': 1.0,
            'high': 2.0,
            'ultra': 4.0
        }
        
        quality_multiplier = quality_multipliers.get(self.config.processing.quality, 1.0)
        processing_time = base_time * quality_multiplier
        
        self.logger.info(f"Processing time estimate: {processing_time:.1f} seconds")
        
        # Simulate actual processing with progress updates
        for i in range(5):
            time.sleep(processing_time / 5)
            progress = (i + 1) * 20
            self.logger.info(f"Progress: {progress}%")
        
        return processing_time
    
    def _dry_run_preview(self) -> bool:
        """Preview operations without executing them."""
        self.logger.info("=== DRY RUN PREVIEW ===")
        
        for i, video_path in enumerate(self.config.video_paths, 1):
            self.logger.info(f"\nVideo {i}: {video_path}")
            
            # Get video info
            video_info = self._get_video_info(video_path)
            output_path = self.config.get_output_path(video_path)
            
            # Calculate parameters
            interpolation_params = self._calculate_interpolation_params(video_info)
            
            # Display preview
            self.logger.info(f"  Input:  {video_path}")
            self.logger.info(f"  Output: {output_path}")
            self.logger.info(f"  FPS:    {video_info['fps']:.2f} → {self.config.processing.target_fps:.2f} "
                           f"(factor: {interpolation_params['factor']:.2f}x)")
            self.logger.info(f"  Quality: {self.config.processing.quality}")
            self.logger.info(f"  Size:   {video_info['size_mb']:.1f} MB")
            
            # Check for conflicts
            if output_path.exists():
                if self.config.force_overwrite:
                    self.logger.info(f"  Status: Will overwrite existing file")
                else:
                    self.logger.warning(f"  Status: Output file exists (use --force-overwrite)")
            else:
                self.logger.info(f"  Status: Ready to process")
        
        self.logger.info(f"\n=== SUMMARY ===")
        self.logger.info(f"Total videos: {len(self.config.video_paths)}")
        self.logger.info(f"Target FPS: {self.config.processing.target_fps}")
        self.logger.info(f"Quality: {self.config.processing.quality}")
        self.logger.info(f"Output format: {self.config.processing.output_format}")
        
        return True