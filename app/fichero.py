from TTS.api import TTS

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2",
    gpu=False
)

tts.tts_to_file(
    text="Hola mundo",
    speaker_wav="voz_referencia.wav",
    file_path="out.wav",
    language="es"
)
