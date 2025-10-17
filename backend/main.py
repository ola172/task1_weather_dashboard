from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.apis.health_route import router as health_router
from backend.constant_manager import ProjectDirectories


app = FastAPI(
    title="Weather Dashboard API",
    description="API for fetching weather data from OpenWeatherMap",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Initialize Jinja2 templates
templates = Jinja2Templates(directory=str(ProjectDirectories.TEMPLATE_DIR))

 # Mount static files directory (CSS, JS, assets)
app.mount("/static", StaticFiles(directory=ProjectDirectories.STATIC_DIR), name="static")
app.include_router(health_router, prefix="/api")

@app.get("/", include_in_schema=False)
async def index(request: Request):
    """Render the main index page."""
    return templates.TemplateResponse("index.html", {"request": request})
