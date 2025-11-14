#! /bin/bash
set -e

if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv..."
    pip install --no-cache-dir uv
else
    echo "✅ uv already installed."
fi

if [ ! -d ".venv" ]; then
    echo "🐍 Creating virtual environment..."
    uv venv
else
    echo "✅ Virtual environment already exists."
fi

if [ -f "pyproject.toml" ]; then
    echo "📚 Installing project dependencies..."
    uv sync --all-groups
else
    echo "⚠️ No pyproject.toml found, skipping dependency installation."
fi

if [ -f ".venv/bin/activate" ]; then
    echo "source /workspaces/saibyo/.venv/bin/activate" >> ~/.zshrc
    echo "✅ Virtual environment added to Zsh startup."
fi

echo ""
echo "✅ Environment summary:"
echo "- Python version: $(python --version)"
echo "- uv version: $(uv --version)"
echo "- Working directory: $(pwd)"
echo ""

echo "🎉 DevContainer setup completed successfully!"