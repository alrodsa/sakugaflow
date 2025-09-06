# 🌀 SakugaFlow: Anime Frame Rate Booster

[![CI - Python UV](https://img.shields.io/badge/CI-Python%20UV-blue?logo=githubactions)](https://github.com/alrodsa/sakugaflow/actions/workflows/python-ci.yml)
[![Publish](https://img.shields.io/badge/Publish-Package-orange?logo=pypi)](https://github.com/alrodsa/sakugaflow/actions/workflows/publish.yml)
[![Release](https://img.shields.io/badge/Release-Automated-green?logo=github)](https://github.com/alrodsa/sakugaflow/actions/workflows/release-please.yml)
[![YouTube Demo](https://img.shields.io/badge/YouTube-Demo-red?logo=youtube)](https://youtu.be/your-demo-link)

![Demo GIF](assets/gifs/anime-fps-demo.gif)

> ⚠️ **IMPORTANT:** The gif above may not reflect the full potential of SakugaFlow.
> Watch the [YouTube Demo](https://youtu.be/your-demo-link) for better results.

## 🔎 Overview

**SakugaFlow** is a Python library designed to **multiply the FPS of anime videos**.
Its main purpose is to make anime scenes smoother by generating intermediate frames using **Deep Learning** techniques.

Typical use cases:

- 🖼️ Boosting 24 FPS anime to 48, 96, 192 FPS or more
- 🎞️ Enhancing sakuga scenes for AMVs or edits
- 🧪 Preparing high-FPS datasets for animation research

### What SakugaFlow Does

The main purpose of SakugaFlow is to take an anime video as input and use the **`exponential`** parameter to determine the FPS multiplier, following this logic:

- `exp=1` → 2× FPS
- `exp=2` → 4× FPS
- `exp=3` → 8× FPS

The output is the high-FPS video saved to a target folder, without changing resolution or restoring quality.

### Features

The main features of SakugaFlow include:

- ✅ Easy-to-use CLI (`douga` command)
- ⚡ GPU acceleration with PyTorch and CUDA.
- 🎛️ Flexible FPS multiplication for anime workflows.

## 🐍 Installation

There are two main ways to install SakugaFlow and its dependencies:

1. Using Devcontainer (recommended for development).
2. In local Python environment.

### Using Devcontainer (Recommended for Development)

To set up the development environment using Devcontainer, follow these steps:

1. Ensure you have [Visual Studio Code](https://code.visualstudio.com/) installed.
2. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
3. Clone the SakugaFlow repository:

   ```bash
    git clone https://github.com/alrodsa/sakugaflow.git
   ```

4. Open the cloned repository in Visual Studio Code.
5. Create an `.env` file in the `.devcontainer` folder with the following variables [^1]:

   ```env
    PYTHON_PASSWORD=token
    ARTIFACT_URL=url
   ```

6. Press `F1` and select `Remote-Containers: Reopen in Container`.

Once these steps are completed, the Devcontainer will build the environment with all necessary dependencies installed.

### In Local Python Environment

To install SakugaFlow in your local Python environment, follow these steps:

1. Clone the SakugaFlow repository:

   ```bash
    git clone https://github.com/alrodsa/sakugaflow.git
   ```

2. Navigate to the cloned directory:

   ```bash
    cd sakugaflow
   ```

3. Create a virtual environment (recommended):

   ```bash
    python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
      venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
      source venv/bin/activate
     ```

5. Export the required environment variables [^1]:

   ```bash
    export PYTHON_PASSWORD=token
    export ARTIFACT_URL=url
    export UV_EXTRA_INDEX_URL="https://_json_key_base64:${PYTHON_PASSWORD}@${ARTIFACT_URL}"
   ```

6. Install `uv`:

   ```bash
    pip install uv
   ```

7. Install **SakugaFlow** dependencies:

   ```bash
    python -m uv sync --all-extras --all-groups
   ```

At the end of this process, you will have SakugaFlow and its dependencies installed in your local Python environment.

> [^1]: **Important:** These variables are required for SakugaFlow to install and use the privative library `saibyo` for frame interpolation, which is not included in the Devcontainer due to licensing restrictions. You will need to install it manually in the Devcontainer terminal. For more information, refer to the [saibyo installation instructions](/docs/guides/install_saibyo.md).

## 🚀 Usage: Boosting Anime FPS

SakugaFlow can be used in two main ways: via the Command-Line Interface (CLI) or programmatically through its API.

### 1️⃣ Command-Line Interface (CLI)

The CLI provides a straightforward way to boost the FPS of anime videos using the `douga`[^2]: command. Here’s how to use it:

```bash
python main.py douga \
    --input_directory=<input_directory> \
    --output_directory=<output_directory> \
    --fps_multiplier=<fps_multiplier>
```

- `<input_directory>`: Path to the video or folder containing videos to process.
- `<output_directory>`: Path to the folder where output videos will be saved.
- `<fps_multiplier>`:  Multiplier for FPS (e.g., `2` for 2×, `4` for 4×, etc.). Take into account that the multiplier must be a power of 2 (i.e., 2, 4, 8, 16, etc.).

> [^2]: **Note:** The word `Douga` **(動画)** means `moving pictures` in Japanese, which is fitting for a tool that enhances video frame rates.

#### Example

To boost the FPS of all videos in the `input_videos` folder by `4×` and save them to the `output_videos` folder, run:

```bash
python main.py douga \
    --input_directory=data-sakugaflow/input \
    --output_directory=data-sakugaflow/output \
    --fps_multiplier=4
```

### 2️⃣ Programmatic API Usage

SakugaFlow can also be used programmatically by importing the necessary classes and functions. Here’s a basic example:

```python
from src.cli.douga import douga

douga(
    input_directory="data-sakugaflow/input",
    output_directory="data-sakugaflow/output",
    fps_multiplier=4
)
```

This will achieve the same result as the CLI example above, boosting the FPS of videos in the specified input directory and saving them to the output directory.

## 📝 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](/LICENSE) file for details.

## 👤 Author

This project and also `saibyo` library are developed and maintained by [Alrodsa](https://github.com/alrodsa).
