#!/usr/bin/env bash
set -e

echo "🚀 Starting post-create setup for sakugaflow..."

# URL of the Artifact Registry
echo "🔑 Configuring Artifact Registry credentials for uv..."
export UV_EXTRA_INDEX_URL="https://_json_key_base64:${PYTHON_PASSWORD}@${ARTIFACT_URL}"

# Ensure the environment variable is set in both zsh and bash
echo "export UV_EXTRA_INDEX_URL=\"https://_json_key_base64:\${PYTHON_PASSWORD}@\${ARTIFACT_URL}\"" >> ~/.zshrc
echo "export UV_EXTRA_INDEX_URL=\"https://_json_key_base64:\${PYTHON_PASSWORD}@\${ARTIFACT_URL}\"" >> ~/.bashrc

# Create .venv if not already present
if [ ! -d ".venv" ]; then
  echo "📦 Creating virtual environment..."
  python -m uv venv .venv
else
  echo "📦 Virtual environment already exists, skipping creation."
fi

# Sync the virtual environment with uv
echo "🔄 Syncing uv extras and groups..."
python -m uv sync --all-extras --all-groups
