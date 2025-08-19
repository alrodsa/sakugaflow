# Douga Command - AI Video Frame Interpolation

The `douga` command provides AI-powered video frame interpolation using the Saibyo library to increase the framerate of video content.

## Features

- 🎥 **Multiple Video Processing**: Process single videos or batches of videos
- ⚙️ **Flexible Configuration**: Command-line options and configuration files
- 🔄 **Frame Interpolation**: AI-powered frame generation for smooth motion
- 📈 **Quality Control**: Multiple quality levels and resolution scaling
- 🎯 **Target FPS or Interpolation Factor**: Choose your preferred method
- 🔍 **Dry Run Mode**: Preview operations before execution
- 📊 **Progress Tracking**: Detailed logging and progress feedback

## Quick Start

### Process a Single Video
```bash
python main.py douga video.mp4
```

### Process Multiple Videos
```bash
python main.py douga '["video1.mp4", "video2.mp4"]' --target_fps 120
```

### Use Glob Patterns
```bash
python main.py douga "episodes/*.mp4" --quality ultra
```

### Use Configuration File
```bash
python main.py douga video.mp4 --config douga_config_example.json
```

## Command-Line Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `videos` | - | str/list | Required | Video file(s) to process |
| `--config` | `-c` | str | None | Configuration file path |
| `--output_dir` | - | str | None | Output directory |
| `--target_fps` | - | float | 60.0 | Target framerate |
| `--quality` | `-q` | str | "high" | Quality level |
| `--interpolation_factor` | `-i` | float | None | Interpolation multiplier |
| `--output_format` | - | str | "mp4" | Output format |
| `--batch_size` | `-b` | int | 1 | Batch processing size |
| `--dry_run` | `-d` | bool | False | Preview mode |
| `--verbose` | `-v` | bool | False | Detailed logging |
| `--force_overwrite` | `-f` | bool | False | Overwrite existing files |
| `--preserve_audio` | `-p` | bool | True | Keep original audio |
| `--use_gpu` | `-u` | bool | True | GPU acceleration |
| `--resolution_scale` | `-r` | float | 1.0 | Resolution scaling |
| `--temp_dir` | - | str | None | Temporary directory |

## Quality Levels

- **`low`**: Fastest processing, basic quality
- **`medium`**: Balanced speed and quality  
- **`high`**: High quality processing (default)
- **`ultra`**: Maximum quality, slower processing

## Output Formats

Supported formats: `mp4`, `avi`, `mkv`, `mov`

## Configuration File

Use JSON, YAML, or TOML configuration files for complex setups. See `douga_config_example.json` for all available options.

## Examples

### High-Quality Anime Processing
```bash
python main.py douga "anime_episode.mp4" \
  --target_fps 144 \
  --quality ultra \
  --resolution_scale 1.5 \
  --output_format mkv
```

### Batch Processing with Custom Output
```bash
python main.py douga "videos/*.mp4" \
  --output_dir "./processed" \
  --quality medium \
  --batch_size 4 \
  --force_overwrite
```

### Preview Operations
```bash
python main.py douga "large_video.mp4" \
  --target_fps 120 \
  --dry_run \
  --verbose
```

### Using Interpolation Factor
```bash
python main.py douga "video.mp4" \
  --interpolation_factor 3.0 \
  --quality high
```

## Output Files

For each processed video, the command generates:
- **Video file**: `{original_name}_interpolated.{format}`
- **Info file**: `{original_name}_interpolated.json` (processing details)

## Error Handling

The command validates:
- Video file existence and format
- Configuration parameters
- Output directory permissions
- Available system resources

Use `--verbose` for detailed error information and `--dry_run` to preview operations safely.