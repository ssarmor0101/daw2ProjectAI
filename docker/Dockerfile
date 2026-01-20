FROM python:3.9.25-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG UID=1001
ARG GID=1001

# Dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
 && rm -rf /var/lib/apt/lists/*

# Crear directorios
RUN mkdir -p /opt/app /opt/models

# Crear usuario
RUN groupadd -g ${GID} appuser && useradd -r -u ${UID} -g appuser appuser \
 && chown -R ${UID}:${GID} /opt/app /opt/models

WORKDIR /opt/app

# Copiar requirements e instalar paquetes
COPY requirements.txt /opt/app/
RUN pip install --no-cache-dir -r /opt/app/requirements.txt

# Cambiar a usuario no root
USER ${UID}:${GID}

# NO COPIAMOS LA APP - se monta con volumen desde Compose
# COPY app/ /opt/app

# CMD por defecto (puedes descomentar cuando quieras usarlo)
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
