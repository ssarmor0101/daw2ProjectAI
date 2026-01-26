from transformers import MarianMTModel, MarianTokenizer

MODELOS = {
    ("es", "en"): "Helsinki-NLP/opus-mt-es-en",
    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
    ("es", "fr"): "Helsinki-NLP/opus-mt-es-fr",
    ("es", "de"): "Helsinki-NLP/opus-mt-es-de",
    ("es", "ru"): "Helsinki-NLP/opus-mt-es-ru",
    # ("es", "ja"): "Helsinki-NLP/opus-mt-es-ja",
}

_cache = {}

def cargar_modelo(origen, destino):
    key = (origen, destino)

    if key not in MODELOS:
        raise ValueError("Idioma no soportado")

    if key not in _cache:
        nombre_modelo = MODELOS[key]
        tokenizer = MarianTokenizer.from_pretrained(nombre_modelo)
        model = MarianMTModel.from_pretrained(nombre_modelo)
        _cache[key] = (tokenizer, model)

    return _cache[key]


def traducir(texto: str, origen: str, destino: str) -> str:
    tokenizer, model = cargar_modelo(origen, destino)
    tokens = tokenizer(texto, return_tensors="pt", padding=True)
    salida = model.generate(**tokens)
    return tokenizer.decode(salida[0], skip_special_tokens=True)
