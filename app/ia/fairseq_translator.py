from ia.base import TranslatorIA
import torch
from fairseq.models.transformer import TransformerModel

class FairseqTranslator(TranslatorIA):
    """
    Clase para traducción usando Fairseq.
    """

    def __init__(self, model_name: str = "transformer.wmt19.en-de"):
        """
        Inicializa el modelo de Fairseq.
        model_name: Nombre del modelo preentrenado de Fairseq.
        """
        # Cargar el modelo preentrenado
        self.model = TransformerModel.from_pretrained(
            model_name_or_path=model_name,
            checkpoint_file='model.pt',
            data_name_or_path=model_name,
            bpe='subword_nmt',     # depende del modelo
            bpe_codes=f'{model_name}/bpecodes'
        )
        # Usar GPU si está disponible
        self.model.cuda() if torch.cuda.is_available() else self.model.cpu()

    def translate(self, text: str, source: str = None, target: str = None) -> str:
        """
        Traduce un texto de un idioma a otro.
        Fairseq preentrenado ya tiene idioma fijo (source->target), pero se pueden
        usar varios modelos para distintos pares.
        """
        return self.model.translate(text)
