from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import districts, stream
from . import models, database
app = FastAPI(title="Maharashtra Security Dashboard Backend")
# Create tables if they don't exist
models.Base.metadata.create_all(bind=database.engine)
# Allow frontend on localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(districts.router, prefix="/api/districts", tags=["districts"])
app.include_router(stream.router, prefix="/api/stream", tags=["stream"])