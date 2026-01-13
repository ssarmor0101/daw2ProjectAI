# Usamos Python 3.9.25 slim
FROM python:3.9.25-slim

# Evitamos prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# Creamos la variable de entorno para el usuario
ENV DOCKER_USER_ID=${UID}

# Instalamos herramientas básicas y dependencias
RUN apt-get update && apt-get install -y --no-install-recommends build-essential git curl sudo python3-dev libpython3.9-dev && rm -rf /var/lib/apt/lists/*

# Creamos un usuario con la misma ID que el host
# RUN useradd -m -u $DOCKER_USER_ID ttsuser && echo "ttsuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Cambiamos al usuario creado
USER $DOCKER_USER_ID

# Actualizamos pip y herramientas de Python
RUN pip install --upgrade pip setuptools wheel

# Instalamos PyTorch CPU y TTS ligero
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install TTS --no-cache-dir --no-deps
RUN pip install torch torchaudio numpy scipy

# Copiamos un script opcional de prueba (si existe)
# COPY --chown=ttsuser:ttsuser ./tts_example.py ./tts_example.py

# Comando por defecto
# CMD ["python", "tts_example.py"]