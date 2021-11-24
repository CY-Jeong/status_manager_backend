

from fastapi import FastAPI

app = FastAPI(
    title="Status Manager",
    description="OS, GPU, MEM Status Manger",
    version="1.0.0",
    openapi_url="/docs/openapi.json"
)
