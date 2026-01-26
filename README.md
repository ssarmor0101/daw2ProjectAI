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

- docker compose --env-file .env.docker build
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

pip install transformers sentencepiece torch

from transformers import MarianMTModel, MarianTokenizer

## 🌍 Idiomas soportados

| Código | Idioma     |
| ------ | ---------- |
| af     | Afrikaans  |
| ar     | Árabe      |
| bg     | Búlgaro    |
| bn     | Bengalí    |
| ca     | Catalán    |
| cs     | Checo      |
| da     | Danés      |
| de     | Alemán     |
| el     | Griego     |
| en     | Inglés     |
| es     | Español    |
| et     | Estonio    |
| fi     | Finés      |
| fr     | Francés    |
| he     | Hebreo     |
| hi     | Hindi      |
| hr     | Croata     |
| hu     | Húngaro    |
| id     | Indonesio  |
| it     | Italiano   |
| ja     | Japonés    |
| ko     | Coreano    |
| lt     | Lituano    |
| lv     | Letón      |
| mk     | Macedonio  |
| nl     | Neerlandés |
| no     | Noruego    |
| pl     | Polaco     |
| pt     | Portugués  |
| ro     | Rumano     |
| ru     | Ruso       |
| sk     | Eslovaco   |
| sl     | Esloveno   |
| sv     | Sueco      |
| ta     | Tamil      |
| th     | Tailandés  |
| tr     | Turco      |
| uk     | Ucraniano  |
| vi     | Vietnamita |
| zh     | Chino      |
