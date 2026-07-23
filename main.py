from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date

from database import engine, SessionLocal,Base
from models import Application

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db(): #cada pedido HTTP que llegue a tu API va a abrir su propia sesión, usarla, y cerrarla automáticamente al terminar 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Antes -----------------------------------|Abajo|
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


@app.get("/")
def inicio():
    return {"mensaje": "JobTrack API funcionando"}

# @app.post("/applications")
# def crear_postulacion(postulacion: Postulacion):
#     if postulacion.id in postulaciones:
#         return {"error": f"Ya existe una postulación con id {postulacion.id}"}

#     postulaciones[postulacion.id] = postulacion
#     return {"mensaje": "Postulación creada", "datos": postulacion}


@app.post("/applications")
def crear_postulacion(postulacion: Postulacion, db: Session = Depends(get_db)):
    existente = db.query(Application).filter(Application.id == postulacion.id).first()
    if existente:
        return {"error": f"Ya existe una postulación con id {postulacion.id}"}

    nueva_postulacion = Application(**postulacion.model_dump())
    db.add(nueva_postulacion)
    db.commit()
    db.refresh(nueva_postulacion)

    return {"mensaje": "Postulación creada", "datos": nueva_postulacion}

@app.get("/applications")
def listar_postulaciones(db: Session = Depends(get_db)):
    return db.query(Application).all()


@app.get("/applications/{id}")
def obtener_postulacion(id: int, db: Session = Depends(get_db)):
    postulacion = db.query(Application).filter(Application.id == id).first()
    if postulacion:
        return postulacion
    return {"error": "Postulación no encontrada"}



@app.put("/applications/{id}")
def actualizar_postulacion(id: int, postulacion_actualizada: Postulacion, db: Session = Depends(get_db)):
    postulacion = db.query(Application).filter(Application.id == id).first()
    if not postulacion:
        return {"error": "Postulación no encontrada"}

    for campo, valor in postulacion_actualizada.model_dump().items():
        setattr(postulacion, campo, valor)

    db.commit()
    db.refresh(postulacion)
    return {"mensaje": "Postulación actualizada", "datos": postulacion}


@app.delete("/applications/{id}")
def eliminar_postulacion(id: int, db: Session = Depends(get_db)):
    postulacion = db.query(Application).filter(Application.id == id).first()
    if not postulacion:
        return {"error": "Postulación no encontrada"}

    db.delete(postulacion)
    db.commit()
    return {"mensaje": f"Postulación {id} eliminada"}