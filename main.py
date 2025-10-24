from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
from dotenv import load_dotenv
load_dotenv()
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY = os.getenv('API_KEY')  # replace with your key

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "weather": None})

@app.post("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Form(...)):
    weather_data = None
    error = None

    async with httpx.AsyncClient() as client:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = await client.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error = "City not found"

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "weather": weather_data, "error": error},
    )
