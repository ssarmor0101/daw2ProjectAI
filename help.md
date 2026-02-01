## Activar el entorno

- Ejecutar el modulo venv
  ``` cmd
  python3.9 -m venv venv
  ```

- Entrar en el entorno
  ``` cmd
  source venv/bin/active
  ```

- Para salir del entorno
  ``` cmd
  deactivate
  ```

## Instalar recursos necesarios

- Instalar paquetes
  ``` cmd
  pip install fastapi
  ```

- Actualizar fichero requirements.txt
  ``` cmd
  pip freeze > requirements.txt
  ```

- Instalar paquetes desde un fichero
  ``` cmd
  pip install -r requirements.txt
  ```

## FastAPI

- Ejecutar la aplicacion con FastAPI
  ``` cmd
  uvicorn fichero:variable --reload
  ```