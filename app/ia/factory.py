from core.config import IA_PROVIDER
from ia.marian_translator import MarianTranslator
from ia.openai_translator import OpenAITranslator
from ia.fairseq_translator import FairseqTranslator

def get_translator():
    if IA_PROVIDER == "openai":
        return OpenAITranslator()
    if IA_PROVIDER == "fairseq":
        return FairseqTranslator()
    return MarianTranslator()
