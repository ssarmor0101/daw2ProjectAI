# Proyecto IA Texto -> Voz

> Trabajo realizado por: Nicolas Navarrete Rios, Antonio Gabriel Portillo Campos, Sergio Sarmiento Moreno \
  DAW 2º 25-26

## Prompts (Eliminar)

Quiero hacer una pagina web con FastAPI con IA para generar un audio en funcion de un texto. ¿Que ficheros necesitare al menos? ¿Como deberia organizarlo? ¿Que modelos de hugging face me recomiendas que sean ligeros?

## Modelos

- facebook/mms-tts-spa

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
