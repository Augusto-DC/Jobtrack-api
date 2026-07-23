from sqlalchemy import Column, Integer, String, Date, ARRAY
from database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    empresa = Column(String, nullable=False)
    puesto = Column(String, nullable=False)
    url_oferta = Column(String)
    modalidad = Column(String)
    ubicacion = Column(String)
    tecnologias = Column(ARRAY(String))
    fecha_publicacion = Column(Date)
    fecha_postulacion = Column(Date)
    estado = Column(String)
    notas = Column(String)