from ia.base import TranslatorIA

class TraduccionService:

    def __init__(self, translator: TranslatorIA):
        self.translator = translator

    def traducir(self, texto: str, origen: str, destino: str) -> str:
        origen = origen.lower()
        destino = destino.lower()

        if not texto.strip():
            raise ValueError("El texto no puede estar vacío")

        return self.translator.translate(texto, origen, destino)
