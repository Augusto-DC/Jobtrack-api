from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class Postulacion(BaseModel):
    empresa: str
    puesto: str
    url_oferta: str
    modalidad: str
    ubicacion: str
    tecnologias: list[str]
    fecha_publicacion: date
    fecha_postulacion: date
    estado: str
    notas: str

@app.get("/")
def inicio():
    return {"mensaje": "JobTrack API funcionando"}

@app.get("/otra-cosa")
def otra_funcion():
    return {"mensaje": "esto es otro endpoint"}

@app.post("/applications")
def crear_postulacion(postulacion: Postulacion):
    return {"mensaje": "Postulación recibida", "datos": postulacion}