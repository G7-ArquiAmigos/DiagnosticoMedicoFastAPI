from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from typing import Optional
from datetime import date
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Modelo de entrada (como el de Django)
class DiagnosticoMedico(BaseModel):
    fecha: date
    tipo: str
    descripcion: str
    recomendaciones: Optional[str] = None
    medico_id: Optional[int] = None
    junta_medica_id: Optional[int] = None

# ruta base Json
@app.get("/")
def root():
    return {"message": "Diagnóstico Médico API funcionando"}

# ruta para POST por Json
@app.post("/diagnostico/")
def crear_diagnostico(data: DiagnosticoMedico):
    # 
    return {
        "mensaje": "Diagnóstico registrado con éxito",
        "datos": data
    }

# ruta para mostrar el formulario HTML
@app.get("/form", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ruta para procesar datos del formulario HTML
@app.post("/diagnostico/form", response_class=HTMLResponse)
def crear_desde_formulario(
    request: Request,
    fecha: str = Form(...),
    tipo: str = Form(...),
    descripcion: str = Form(...),
    recomendaciones: str = Form(None),
    medico_id: Optional[int] = Form(None),
    junta_medica_id: Optional[int] = Form(None),
):
    datos = {
        "fecha": fecha,
        "tipo": tipo,
        "descripcion": descripcion,
        "recomendaciones": recomendaciones,
        "medico_id": medico_id,
        "junta_medica_id": junta_medica_id
    }
    return templates.TemplateResponse("index.html", {
        "request": request,
        "resultado": datos
    })


