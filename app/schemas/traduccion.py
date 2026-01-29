from ia.base import TranslatorIA

class TraduccionService:
    def __init__(self, translator: TranslatorIA):
        self.translator = translator

    def traducir(self, texto: str, origen: str, destino: str) -> str:
        return self.translator.translate(texto, origen, destino)
