from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates/calculate"))

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def calc_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})


class Numbers(BaseModel):
    num1: float
    num2: float


def form_to_model(num1: float = Form(...), num2: float = Form(...)) -> Numbers:
    return Numbers(num1=num1, num2=num2)


@app.post("/", response_class=HTMLResponse)
def calc(request: Request, data: Numbers = Depends(form_to_model)):
    return templates.TemplateResponse("index.html", {"request": request, "sum": data.num1 + data.num2})
