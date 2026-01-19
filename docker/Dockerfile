# Usamos Python 3.9.25 slim
FROM python:3.9.25-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dependencias del sistema (solo build-time)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    python3-dev \
    libpython3.9-dev \
 && rm -rf /var/lib/apt/lists/*

# Directorios de trabajo
RUN mkdir -p /opt/app /opt/models \
 && chown -R ${UID}:${GID} /opt/app /opt/models

# Usar UID/GID externos (aunque no existan en el contenedor)
USER ${UID}:${GID}

WORKDIR /opt/app

# pip en modo usuario
ENV PATH="/home/.local/bin:${PATH}"

# Actualizar pip
RUN pip install --user --upgrade pip setuptools wheel

# PyTorch CPU
RUN pip install --user torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/cpu

# TTS y deps
RUN pip install --user TTS numpy scipy