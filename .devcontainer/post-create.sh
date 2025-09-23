#!/usr/bin/env bash
set -e

echo "🚀 Starting post-create setup for sakugaflow..."

# URL of the Artifact Registry
echo "🔑 Configuring Artifact Registry credentials for uv..."
export UV_EXTRA_INDEX_URL="https://_json_key_base64:${PYTHON_PASSWORD}@${ARTIFACT_URL}"

echo "export UV_EXTRA_INDEX_URL=\"https://_json_key_base64:\${PYTHON_PASSWORD}@\${ARTIFACT_URL}\"" >> ~/.zshrc
echo "export UV_EXTRA_INDEX_URL=\"https://_json_key_base64:\${PYTHON_PASSWORD}@\${ARTIFACT_URL}\"" >> ~/.bashrc

# Check if 'uv' is installed, if not install it for the current user
if ! command -v uv >/dev/null 2>&1; then
  echo "⚠️  'uv' is not installed. Installing 'uv' for the current user..."
  python3 -m pip install --user --no-cache-dir uv
  export PATH="$HOME/.local/bin:$PATH"
fi

# Create .venv if not already present
if [ ! -d ".venv" ]; then
  echo "📦 Creating virtual environment..."
  uv venv .venv
else
  echo "📦 Virtual environment already exists, skipping creation."
fi

echo 'export VENV="/workspaces/sakugaflow/.venv"' >> ~/.bashrc
echo 'export PATH="$VENV/bin:$HOME/.local/bin:$PATH"' >> ~/.bashrc
echo 'export VENV="/workspaces/sakugaflow/.venv"' >> ~/.zshrc
echo 'export PATH="$VENV/bin:$HOME/.local/bin:$PATH"' >> ~/.zshrc

# Activate the virtual environment
source .venv/bin/activate

echo "🔄 Syncing uv extras and groups..."
uv sync --all-extras --all-groups
