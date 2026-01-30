import torch
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
from ia.base import TranslatorIA

MODEL_NAME = "facebook/m2m100_418M"

# Idiomas soportados (puedes ampliar)
IDIOMAS = {"en", "es", "fr", "de", "it", "ja", "zh"}

class M2M100Translator(TranslatorIA):

    _model = None
    _tokenizer = None

    def _load_model(self):
        if self._model is None or self._tokenizer is None:
            self._tokenizer = M2M100Tokenizer.from_pretrained(MODEL_NAME)
            self._model = M2M100ForConditionalGeneration.from_pretrained(MODEL_NAME)
            self._model.eval()  # importante en CPU

        return self._tokenizer, self._model

    def translate(self, text: str, source: str, target: str) -> str:
        if source not in IDIOMAS or target not in IDIOMAS:
            raise ValueError("Idioma no soportado")

        tokenizer, model = self._load_model()

        tokenizer.src_lang = source
        tokens = tokenizer(text, return_tensors="pt", padding=True)

        with torch.no_grad():
            output = model.generate(
                **tokens,
                forced_bos_token_id=tokenizer.get_lang_id(target),
                num_beams=3  # mejor para CPU
            )

        return tokenizer.decode(output[0], skip_special_tokens=True)
