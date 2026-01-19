from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from TTS.api import TTS
import os
import uuid

MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
MODELS_PATH = "/opt/models"
OUTPUT_PATH = "/opt/app/output"

os.makedirs(OUTPUT_PATH, exist_ok=True)

app = FastAPI(title="XTTS v2 API")

# Cargar modelo UNA vez al arrancar
tts = TTS(
    model_name=MODEL_NAME,
    gpu=False,
    progress_bar=False,
    cache_path=MODELS_PATH,
)

class TTSRequest(BaseModel):
    text: str
    language: str = "es"
    speaker_wav: str  # path a wav dentro del contenedor

@app.post("/tts")
def synthesize(req: TTSRequest):
    if not os.path.exists(req.speaker_wav):
        raise HTTPException(status_code=400, detail="speaker_wav no existe")

    output_file = f"{OUTPUT_PATH}/{uuid.uuid4()}.wav"

    tts.tts_to_file(
        text=req.text,
        speaker_wav=req.speaker_wav,
        language=req.language,
        file_path=output_file,
    )

    return {"output_wav": output_file}
