# Proyecto IA Texto -> Voz

> Trabajo realizado por: Nicolas Navarrete Rios, Antonio Gabriel Portillo Campos, Sergio Sarmiento Moreno \
  DAW 2º 25-26

> Python 3.9.25

## Activar el entorno

- Ejecutar el modulo venv
  ``` cmd
  python3 -m venv venv
  ```

- Entrar en el entorno
  ``` cmd
  source venv/bin/active
  ```

- Para salir del entorno
  ``` cmd
  deactivate
  ```

## Instalar recursos necesarios

- Instalar paquetes
  ``` cmd
  pip install fastapi
  ```

- Actualizar fichero requirements.txt
  ``` cmd
  pip freeze > requirements.txt
  ```

- Instalar paquetes desde un fichero
  ``` cmd
  pip install -r requirements.txt
  ```

## FastAPI

- Ejecutar la aplicacion con FastAPI
  ``` cmd
  uvicorn fichero:variable --reload
  ```

## Docker

- docker compose --env-file .env.docker up -d

## Modelos

- facebook/mms-tts-spa
- coqui/XTTS-v2

## Arquitectura

### 1

``` txt
project/
│
├── app/
│   ├── main.py              # FastAPI app
│   │
│   ├── api/
│   │   └── routes.py        # Endpoints
│   │
│   ├── services/
│   │   └── tts_service.py   # Generación de audio
│   │
│   ├── core/
│   │   └── config.py        # Settings (paths, modelo, etc.)
│   │
│   └── models/
│       └── tts_model.py     # Carga y wrapper del modelo HF
│
├── static/
│   └── audio/
│
├── templates/
│   └── index.html
│
├── requirements.txt
└── .env
```

## Bibliografia

- [coqui/XTTS-v2 Installation](https://docs.coqui.ai/en/latest/)