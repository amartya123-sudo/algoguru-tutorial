from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.execute import router as execute_router
from app.api.projects import router as projects_router
from app.api.progress import router as progress_router
from app.api.jobs import router as jobs_router


app = FastAPI(
    title="AlgoGuru API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    projects_router,
    prefix="/projects",
    tags=["Projects"],
)

app.include_router(
    execute_router,
    prefix="/execute",
    tags=["Execution"],
)

app.include_router(
    progress_router,
    prefix="/progress",
    tags=["Progress"],
)

app.include_router(
    jobs_router,
    prefix="/jobs",
    tags=["Jobs"],
)

@app.get("/")
def root():
    return {
        "name": "AlgoGuru API",
        "status": "running",
        "version": "1.0.0",
    }