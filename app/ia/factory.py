from core.config import IA_PROVIDER
from ia.marian_translator import MarianTranslator
from ia.openai_translator import OpenAITranslator
from ia.m2m100_translator import M2M100Translator

def get_translator():
    if IA_PROVIDER == "openai":
        return OpenAITranslator()
    if IA_PROVIDER == "m2m100":
        return M2M100Translator()
    return MarianTranslator()
