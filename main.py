from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()

# Modelo de entrada (como el de Django)
class DiagnosticoMedico(BaseModel):
    fecha: date
    tipo: str
    descripcion: str
    recomendaciones: Optional[str] = None
    medico_id: Optional[int] = None
    junta_medica_id: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Diagnóstico Médico API funcionando"}

@app.post("/diagnostico/")
def crear_diagnostico(data: DiagnosticoMedico):
    # Aquí podrías guardar en BD, pero por ahora solo respondemos
    return {
        "mensaje": "Diagnóstico registrado con éxito",
        "datos": data
    }
