FROM python:3.9.25-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG UID=1001
ARG GID=1001

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    python3-dev \
 && rm -rf /var/lib/apt/lists/*

# Directorios
RUN mkdir -p /opt/app /opt/models \
 && chown -R ${UID}:${GID} /opt/app /opt/models

USER ${UID}:${GID}
WORKDIR /opt/app

ENV PATH="/home/.local/bin:${PATH}"

# Copiar requirements primero (cache)
COPY --chown=${UID}:${GID} requirements.txt .

# INSTALA DIRECTAMENTE sin --user
RUN pip install -r requirements.txt

# Copiar el resto de la app
# COPY --chown=${UID}:${GID} app/ /opt/app

# EXPOSE 8000

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
