![Sakugaflow Logo](assets/images/sakugaflow-logo-light.png#gh-light-mode-only)

![Sakugaflow Logo Dark](assets/images/sakugaflow-logo-dark.png#gh-dark-mode-only)



<p align="center">
  <!-- Lint -->
  <a href="https://github.com/alrodsa/sakugaflow/actions/workflows/python-ci.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/alrodsa/sakugaflow/python-ci.yml?branch=main&label=Lint&logo=github&logoColor=white&style=for-the-badge" alt="Lint Status"/>
  </a>
  <!-- Coverage -->
  <a href="https://codecov.io/gh/alrodsa/sakugaflow">
    <img src="https://img.shields.io/codecov/c/github/alrodsa/sakugaflow?logo=codecov&logoColor=white&style=for-the-badge" alt="Coverage"/>
  </a>
  <!-- CI workflow -->
  <a href="https://github.com/alrodsa/sakugaflow/actions/workflows/python-ci.yml">
  <img src="https://img.shields.io/github/actions/workflow/status/alrodsa/sakugaflow/python-ci.yml?label=CI&logo=githubactions&logoColor=white&style=for-the-badge" alt="CI Status"/>
  </a>
  <!-- Python version -->
  <img src="https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=white&style=for-the-badge" alt="Python Version"/>
  <!-- Linter info -->
  <img src="https://img.shields.io/badge/linter-ruff-yellow?logo=ruff&logoColor=white&style=for-the-badge" alt="Linter"/>
  <!-- License -->
   <a href="https://www.apache.org/licenses/LICENSE-2.0">
      <img src="https://img.shields.io/badge/license-Apache%202.0-green?logo=apache&logoColor=white&style=for-the-badge" alt="License: Apache 2.0"/>
   </a>
  <!-- Demo Video -->
   <a href="https://mega.nz/embed/PVcWCDJQ#u6gkFD4JhAW7XH5r2-y_phBidhWlTHPT6veYnhvuAhU">
      <img src="https://img.shields.io/badge/Video-Demo-red?logo=mega&logoColor=white&style=for-the-badge" alt="Demo Video on MEGA"/>
   </a>
</p>


![Demo GIF](assets/images/anime-fps-demo.gif)

> ⚠️ **IMPORTANT:** The gif above may not reflect the full potential of SakugaFlow (gifs have lower FPS and quality).
> Please **watch/download** the [Video Demo](https://mega.nz/embed/PVcWCDJQ#u6gkFD4JhAW7XH5r2-y_phBidhWlTHPT6veYnhvuAhU) to see the real results.

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

To install SakugaFlow dependencies there are two main options: using a **Devcontainer** (recommended) or installing it in your local Python environment.

### Option 1: Using Devcontainer (Recommended)

1. Ensure you have **Docker** and **VSCode** installed with the **Dev Containers** extension.

2. Clone the SakugaFlow repository:

   ```bash
    git clone https://github.com/alrodsa/sakugaflow.git
   ```

3. Open the repository in VSCode.
4. Reopen the folder in the Devcontainer:

   - Press `F1` and select `Dev Containers: Reopen in Container`.

5. Once the Devcontainer is built and running all dependencies will be installed automatically.

### Option 2: Local Python Environment

1. Ensure you have **Python 3.12+** installed on your system.

2. Clone the SakugaFlow repository:

   ```bash
    git clone https://github.com/alrodsa/sakugaflow.git
    cd sakugaflow
   ```

3. Install `uv` package manager with pip:

   ```bash
      pip install --no-cache-dir uv
   ```

4. Create and activate a virtual environment with `uv`:

   ```bash
      uv venv
   ```

5. Install all dependencies with `uv`:

   ```bash
    uv sync --all-groups
   ```

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

## ☁️ Future Cloud Architecture (Planned)

SakugaFlow aims to support a complete **cloud-native anime interpolation pipeline**, enabling automated FPS boosting for full episodes using scalable GPU infrastructure on Google Cloud.

### 🔹 1. Cloud Run — Public API Layer
Cloud Run will expose secure endpoints:

- `POST /interpolate` → upload video or provide a GCS path  
- `GET /status/{job_id}` → check inference progress  
- `GET /result/{job_id}` → retrieve output metadata  

**Responsibilities:**
- Validate requests  
- Upload video to GCS  
- Trigger Vertex AI job with dynamic parameters  
- Return a `job_id` for polling  

### 🔹 2. Vertex AI — On-Demand GPU Inference

When Cloud Run receives a request:

1. A **Vertex AI Custom Job** is created dynamically  
2. The job spins up a GPU instance (A2, L4, etc.)  
3. Runs Saibyo interpolation inside a container  
4. Saves the output video to a dedicated GCS bucket  
5. Emits progress updates via Pub/Sub  

**Parameters sent from Cloud Run to Vertex AI:**

- `EXP` (fps multiplier)  
- `LIGHTWEIGHT` (fp16 or fp32)  
- `MODEL_VERSION`  
- `INPUT_PATH`, `OUTPUT_PATH`  
- `PUBSUB_TOPIC`  

This ensures **autoscaling**, **zero idle GPU cost**, and **predictable pricing**.

### 🔹 3. Pub/Sub — Job Progress Stream

Vertex AI publishes status events:

- `QUEUED`  
- `STARTED`  
- `INFERENCE`  
- `WRITING_OUTPUT`  
- `DONE` / `FAILED`  

Cloud Run ingests them into a **state cache** (Firestore or Redis) for fast API responses.

### 🔹 4. GCS Buckets — Storage Layer

Two buckets are planned:

| Bucket | Description |
|--------|-------------|
| `anime-input/` | Raw uploads from clients |
| `anime-output/` | FPS-boosted videos generated by Vertex AI |

Each output entry includes:

- Final video (`.mp4`)  
- Metadata (`fps`, duration, exp, model version)  
- Logs  

### 🔹 5. High-Level Workflow Summary

1. Client uploads vídeo → **Cloud Run**  
2. Cloud Run validates + stores input in **GCS**  
3. Cloud Run triggers **Vertex AI GPU job**  
4. Vertex AI runs **Saibyo** → writes output to GCS  
5. Job emits state updates via **Pub/Sub**  
6. Cloud Run stores progress in **Firestore/Redis**  
7. Client polls `/status/{job_id}` + `/result/{job_id}`  

### 📈 Cloud Architecture Diagram

<p align="center">
  <img src="assets/images/cloud-architecture.png" width="100%" />
</p>


## 📝 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](/LICENSE) file for details.

## 👤 Author

**Alvaro R** - [alrodsa](https://github.com/alrodsa).
