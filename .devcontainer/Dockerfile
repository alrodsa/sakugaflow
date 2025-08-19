FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt install -y \
    git \
    python3-pip \
    zsh \
    wget \
    apt-transport-https \
    ca-certificates \
    python3-tk \
    curl \
    lsb-release \
    software-properties-common \
    ffmpeg \
    libsm6 \
    libxext6 \
    libimage-exiftool-perl \
    libvulkan1 \
    vulkan-tools \
    libvulkan-dev \
    libx264-dev \
    libx265-dev \
    libfdk-aac-dev \
    libmp3lame-dev \
    yasm \
    build-essential \
    libopenh264-dev


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





