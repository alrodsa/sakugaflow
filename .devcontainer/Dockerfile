FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MPLBACKEND=Agg

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    bash-completion \
    build-essential \
    ca-certificates \
    curl \
    ffmpeg \
    git \
    libdbus-1-3 \
    libgl1 \
    libglib2.0-0 \
    libgomp1 \
    libimage-exiftool-perl \
    libsm6 \
    libxext6 \
    libxkbcommon0 \
    lsb-release \
    wget \
    yasm \
    zsh \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir uv

ARG USERNAME=sakugaflow
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG RENDER_GID=110

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && getent group render || groupadd -g $RENDER_GID render \
    && usermod -aG render $USERNAME

USER $USERNAME

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t robbyrussell
