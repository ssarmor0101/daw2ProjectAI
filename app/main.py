from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from translator import traducir

app = FastAPI(title="IA Traductor")

class TraduccionRequest(BaseModel):
    texto: str
    origen: str
    destino: str

@app.post("/traducir")
def traducir_endpoint(data: TraduccionRequest):
    try:
        resultado = traducir(
            texto=data.texto,
            origen=data.origen,
            destino=data.destino
        )
        return {
            "texto_original": data.texto,
            "traduccion": resultado
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
