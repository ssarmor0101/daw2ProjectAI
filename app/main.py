from fastapi import FastAPI

# 1. Crear la instancia de la aplicación
app = FastAPI()

# 2. Usar un decorador para definir una ruta (endpoint)
@app.get("/") # Decorador para el método GET en la ruta "/"
async def read_root():
    # 3. La lógica de la función
    # FastAPI convertirá este diccionario en JSON
    return {"message": "¡Bienvenido a mi primera API con FastAPI!"}