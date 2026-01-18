import uvicorn
from fastapi import FastAPI

from backend.src.routes.auth.auth_route import auth_router
from backend.src.routes.models.user_route import user_router

app = FastAPI()

API_PREFIX = "/api"
app.include_router(user_router, prefix=API_PREFIX)
app.include_router(auth_router, prefix=API_PREFIX)

if __name__ == "__main__":
    uvicorn.run(app)
