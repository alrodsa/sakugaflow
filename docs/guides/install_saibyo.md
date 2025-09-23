# 🎬 Saibyo Library: AI-powered Frame Interpolation Tool

Saibyo is a Deep Learning tool designed to **boost the framerate of anime and other kind of video content**, creating smooth motion by interpolating frames with deep learning models.
It is the core library used by [sakugaflow](../../README.md) to **transform anime episodes into higher FPS experiences** *(e.g., 24fps → 50fps, 90fps or even 144fps)*.


## ✨ Features

- 🌀 Frame **interpolation** powered by **Deep Neural Networks**.
- 🎥 Designed for **anime**, but works with general video content.
- 🔧 Export results in standard formats (e.g. `.mp4`).
- ⚡ Integration with `sakugaflow` CLI (`douga` command).

## 📦 Installation

Saibyo is published privately to **Google Artifact Registry**. So before installing, you need to have the right credentials and environment setup.

### Prerequisites

1. **[`PYTHON_PASSWORD`]** A service account with the `Artifact Registry Reader` role and its JSON key. Once you have this, you can encode it in base64.

    ```bash
        cat service-account.json | base64 -w0
        # This will output a long string like (that is your `PYTHON_PASSWORD`):
        # eyJsadf7GH9H90jsd88J...More characters...==
    ```

2. **[`ARTIFACT_URL`]** Getting the `Sakugaflow` `Google Artifact Registry` URL, which is the private repository where Saibyo is hosted.

    ```bash
        export ARTIFACT_URL=region-python.pkg.dev/sakugaflow-project/dev-python/simple
    ```

### Installation Methods

To install `Saibyo`, you can do it in two ways:

1. **Using .devcontainer environment**
If you are using the `.devcontainer` setup, Saibyo is already included in the `pyproject.toml` file. To install it, you only need to set up the environment variables as described below inside your `.env` file (located inside the `.devcontainer` folder):

```bash
PYTHON_PASSWORD=eyJsadf7GH9H90jsd88J...More characters...==
ARTIFACT_URL=region-python.pkg.dev/sakugaflow-project/dev-python/simple
```

After setting up the environment variables, `Build` or `Rebuild` your devcontainer in `VSCode`. This will automatically install `Saibyo` and its dependencies.

2. **Using `uv` package manager**

If you prefer to install `Saibyo` manually, you can use the `uv` package manager. Follow these steps:

- Ensure you have the `uv` package manager installed. If not, you can install it via pip:

```bash
pip install uv
```

- Set the environment variables in your terminal or `.env` file:

```bash
export PYTHON_PASSWORD=eyJsadf7GH9H90jsd88J...More characters...==
export ARTIFACT_URL=region-python.pkg.dev/sakugaflow-project/dev-python/simple
```

- Then, run the following command to export the `UV_EXTRA_INDEX_URL`:

```bash
export UV_EXTRA_INDEX_URL="https://_json_key_base64:${PYTHON_PASSWORD}@${ARTIFACT_URL}"
```

- Once the environment is set up, add the `saibyo` package to your project using `uv`:

```bash
uv add saibyo
```

- Finally, install `Saibyo` using `uv`:

```bash
uv sync
```

After running these commands, `Saibyo` will be installed in your environment, and you can start using it in Sakugaflow or any other Python project.

> 💡 ***Note:** Saibyo is a private package. External users will need valid credentials to install it. The administrator is the one who created Sakugaflow and can provide access.*
