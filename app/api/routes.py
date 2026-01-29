# from ia.factory import get_translator
# from services.traduccion_service import TraduccionService

# translator = get_translator()
# service = TraduccionService(translator)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.traduccion_service import TraduccionService
from ia.factory import get_translator

router = APIRouter()  # 🔹 Esto es lo que se importa

translator = get_translator()
service = TraduccionService(translator)

class TraduccionRequest(BaseModel):
    texto: str
    origen: str
    destino: str

@router.post("/traducir")
def traducir_endpoint(data: TraduccionRequest):
    try:
        resultado = service.traducir(data.texto, data.origen, data.destino)
        return {"texto_original": data.texto, "traduccion": resultado}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
