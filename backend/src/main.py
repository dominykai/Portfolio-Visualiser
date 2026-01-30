from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from backend.src.routes.auth.auth_route import auth_router
from backend.src.routes.models.api_key_route import api_key_router
from backend.src.routes.models.user_route import user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run before program termination

    yield
    # Run after program termination

app = FastAPI(lifespan=lifespan)

API_PREFIX = "/api"
app.include_router(user_router, prefix=API_PREFIX)
app.include_router(auth_router, prefix=API_PREFIX)
app.include_router(api_key_router, prefix=API_PREFIX)

if __name__ == "__main__":
    uvicorn.run(app)
