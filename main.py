from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class Postulacion(BaseModel):
    id: int
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

# Nuestra "base de datos" temporal: un diccionario en memoria (clave = id)
postulaciones: dict[int, Postulacion] = {}

@app.get("/")
def inicio():
    return {"mensaje": "JobTrack API funcionando"}

@app.post("/applications")
def crear_postulacion(postulacion: Postulacion):
    if postulacion.id in postulaciones:
        return {"error": f"Ya existe una postulación con id {postulacion.id}"}

    postulaciones[postulacion.id] = postulacion
    return {"mensaje": "Postulación creada", "datos": postulacion}

@app.get("/applications")
def listar_postulaciones():
    return list(postulaciones.values())

@app.get("/applications/{id}")
def obtener_postulacion(id: int):
    if id in postulaciones:
        return postulaciones[id]
    return {"error": "Postulación no encontrada"}


@app.put("/applications/{id}")
def actualizar_postulacion(id: int, postulacion_actualizada: Postulacion):
    if id not in postulaciones:
        return {"error": "Postulación no encontrada"}

    postulaciones[id] = postulacion_actualizada
    return {"mensaje": "Postulación actualizada", "datos": postulacion_actualizada}

@app.delete("/applications/{id}")
def eliminar_postulacion(id: int):
    if id not in postulaciones:
        return {"error": "Postulación no encontrada"}

    del postulaciones[id]
    return {"mensaje": f"Postulación {id} eliminada"}