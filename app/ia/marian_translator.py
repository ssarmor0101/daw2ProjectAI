import torch
from transformers import MarianMTModel, MarianTokenizer
from ia.base import TranslatorIA

MODELOS = {
    ("es", "en"): "Helsinki-NLP/opus-mt-es-en",
    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
    ("la", "es"): "Helsinki-NLP/opus-mt-la-es",
}

class MarianTranslator(TranslatorIA):

    _cache = {}

    def _load_model(self, source: str, target: str):
        key = (source, target)

        if key not in MODELOS:
            raise ValueError("Idioma no soportado")

        if key not in self._cache:
            name = MODELOS[key]
            tokenizer = MarianTokenizer.from_pretrained(name)
            model = MarianMTModel.from_pretrained(name)
            self._cache[key] = (tokenizer, model)

        return self._cache[key]

    def translate(self, text: str, source: str, target: str) -> str:
        tokenizer, model = self._load_model(source, target)
        tokens = tokenizer(text, return_tensors="pt", padding=True)

        with torch.no_grad():
            output = model.generate(**tokens)

        return tokenizer.decode(output[0], skip_special_tokens=True)
