# Traductor IA - Traducción Automática Inteligente

> **Proyecto desarrollado por:** Nicolas Navarrete Rios, Antonio Gabriel Portillo Campos, Sergio Sarmiento Moreno  
> **Nivel:** DAW 2º 25-26  
> **Versión Python:** 3.9.25

## 📋 Descripción del Proyecto

Este proyecto es una aplicación web de **traducción automática** basada en **modelos de inteligencia artificial** de última generación. La aplicación proporciona una API REST construida con FastAPI que permite traducir textos entre múltiples idiomas utilizando redes neuronales preentrenadas de Hugging Face.

La solución es **escalable, modular y flexible**, permitiendo cambiar entre diferentes modelos de traducción sin modificar el código de la aplicación.

---

## 🏗️ Arquitectura

La aplicación sigue una arquitectura **en capas** bien definida que separa responsabilidades:

```
project/
│
├── app/
│   ├── main.py                  # Configuración y arranque de FastAPI
│   │
│   ├── api/
│   │   └── routes.py            # Endpoints REST (POST /traducir)
│   │
│   ├── services/
│   │   └── traduccion_service.py  # Lógica de negocio de traducción
│   │
│   ├── ia/
│   │   ├── base.py              # Interfaz abstracta TranslatorIA
│   │   ├── factory.py           # Factory Pattern para instanciar traductores
│   │   ├── marian_translator.py # Implementación con modelo Marian
│   │   └── m2m100_translator.py # Implementación con modelo M2M-100
│   │
│   ├── core/
│   │   └── config.py            # Configuración y variables de entorno
│   │
│   └── schemas/
│       └── traduccion.py        # Esquemas Pydantic para validación
│
├── templates/
│   ├── index.html               # Interfaz web
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
│
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Este archivo
```

### Capas de la Arquitectura

1. **API Layer (routes.py)**
   - Define los endpoints REST
   - Valida las peticiones de entrada
   - Maneja errores HTTP

2. **Service Layer (traduccion_service.py)**
   - Contiene la lógica de negocio
   - Valida entrada de datos (textos no vacíos)
   - Orquesta la traducción

3. **IA Layer (ia/)**
   - Abstracción mediante interfaz `TranslatorIA`
   - Implementaciones específicas de modelos
   - Carga y caché de modelos

4. **Core Layer (config.py)**
   - Gestión centralizada de configuración
   - Variables de entorno

---

## 🎯 Patrones de Diseño

### 1. **Strategy Pattern**
La interfaz `TranslatorIA` define el contrato que deben cumplir todos los traductores. Esto permite cambiar la estrategia de traducción (Marian vs M2M-100) de forma dinámica.

```python
# Interfaz abstracta
class TranslatorIA(ABC):
    @abstractmethod
    def translate(self, text: str, source: str, target: str) -> str:
        pass

# Implementaciones intercambiables
class MarianTranslator(TranslatorIA):
    def translate(self, ...): ...

class M2M100Translator(TranslatorIA):
    def translate(self, ...): ...
```

### 2. **Factory Pattern**
El módulo `factory.py` encapsula la creación de instancias de traductores basándose en la variable de entorno `IA_PROVIDER`.

```python
def get_translator():
    if IA_PROVIDER == "m2m100":
        return M2M100Translator()
    return MarianTranslator()  # Por defecto
```

**Ventaja:** Cambiar de modelo solo requiere cambiar la variable de entorno, sin tocar el código.

### 3. **Dependency Injection**
El servicio `TraduccionService` recibe el traductor como dependencia en el constructor, no lo instancia directamente.

```python
class TraduccionService:
    def __init__(self, translator: TranslatorIA):
        self.translator = translator  # Inyección de dependencia
```

### 4. **Singleton Pattern (Caché de Modelos)**
Los traductores mantienen en caché los modelos cargados para evitar recargas innecesarias:

```python
class MarianTranslator(TranslatorIA):
    _cache = {}  # Almacena modelos ya cargados
    
    def _load_model(self, source: str, target: str):
        if key not in self._cache:
            # Carga solo si no existe en caché
            self._cache[key] = (tokenizer, model)
```

---

## 🤖 Integración de la IA

### Modelos Utilizados

#### 1. **Helsinki NLP Marian (Por defecto)**
- **Modelo:** OpusMT (Helsinki-NLP)
- **Tipo:** Modelos específicos por pares de idiomas
- **Ejemplos:**
  - `Helsinki-NLP/opus-mt-es-en` (Español → Inglés)
  - `Helsinki-NLP/opus-mt-en-es` (Inglés → Español)
  - `Helsinki-NLP/opus-mt-la-es` (Latín → Español)

**Ventajas:**
- Modelos ligeros y rápidos
- Especializados por par de idiomas
- Excelente calidad de traducción

**Desventajas:**
- Requiere un modelo diferente para cada par de idiomas

#### 2. **Facebook M2M-100**
- **Modelo:** `facebook/m2m100_418M`
- **Tipo:** Un único modelo multilingüe para 100 idiomas
- **Idiomas soportados:** en, es, fr, de, it, ja, zh (ampliable)

**Ventajas:**
- Un modelo único para múltiples idiomas
- Flexible y expansible

**Desventajas:**
- Más pesado en memoria
- Puede ser más lento en máquinas con recursos limitados

### Flujo de Ejecución de la IA

```
Usuario envía petición JSON
    ↓
API Route (routes.py)
    ↓
TraduccionService valida entrada
    ↓
Factory selecciona el traductor (Marian o M2M-100)
    ↓
Traductor carga modelo (o usa caché)
    ↓
Tokenización del texto
    ↓
Procesamiento por la red neuronal
    ↓
Generación de tokens de salida
    ↓
Decodificación a texto
    ↓
Respuesta JSON al usuario
```

### Tecnologías de IA

- **Framework:** Transformers (Hugging Face)
- **Framework de Deep Learning:** PyTorch
- **GPU:** Soporte para CUDA 12.1 (nvidia-cuda packages)
- **Precisión:** FP32 (puede optimizarse con quantización)

---

## 🚀 Cómo Usar

### Instalación

```bash
# Clonar el repositorio
git clone [url-repositorio]
cd daw2ProjectAI

# Instalar dependencias
pip install -r requirements.txt
```

### Variables de Entorno

```bash
# .env o variables del sistema
IA_PROVIDER=marian      # o "m2m100"
```

### Ejecutar la Aplicación

```bash
# Desde la raíz del proyecto
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

La aplicación estará disponible en `http://localhost:8000`

### Usar la API

#### Endpoint: POST /traducir

**Request:**
```json
{
    "texto": "Hola mundo",
    "origen": "es",
    "destino": "en"
}
```

**Response:**
```json
{
    "texto_original": "Hola mundo",
    "traduccion": "Hello world"
}
```

#### Códigos de Idiomas Soportados

**Marian (Helsinki-NLP):**
- Pares soportados: (es, en), (en, es), (la, es)
- Expandible con más modelos

**M2M-100:**
- en: Inglés
- es: Español
- fr: Francés
- de: Alemán
- it: Italiano
- ja: Japonés
- zh: Chino

---

## 📦 Dependencias Principales

| Paquete | Versión | Propósito |
|---------|---------|-----------|
| fastapi | 0.128.0 | Framework web REST |
| pydantic | 2.12.5 | Validación de datos |
| transformers | 4.57.6 | Modelos de IA (Hugging Face) |
| torch | 2.8.0 | Framework de Deep Learning |
| numpy | 2.0.2 | Computación numérica |

---

## 🔗 Referencias y Bibliografía

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Transformers - Hugging Face](https://huggingface.co/docs/transformers/)
- [Helsinki-NLP Marian Models](https://huggingface.co/Helsinki-NLP)
- [Facebook M2M-100 Model](https://huggingface.co/facebook/m2m100_418M)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)

---

## 👥 Autores

- **Nicolas Navarrete Rios**
- **Antonio Gabriel Portillo Campos**
- **Sergio Sarmiento Moreno**

**Institución:** Ciclo Formativo DAW (Desarrollo de Aplicaciones Web) 2º Año  
**Curso:** 2025-2026