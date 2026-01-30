from contextlib import asynccontextmanager

import logging
import uvicorn
from fastapi import FastAPI

from backend.src.database.crud.broker_crud import preload_db_brokers_table_from_csv
from backend.src.database.db import get_db
from backend.src.routes.auth.auth_route import auth_router
from backend.src.routes.models.api_key_route import api_key_router
from backend.src.routes.models.user_route import user_router

logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run before program termination
    logging.info("Starting Lifespan")

    db_session = next(get_db()) # No access to dependency injection yet

    preload_db_brokers_table_from_csv(db_session)
    logging.info("Preloaded Brokers table from CSV file")

    yield
    # Run after program termination

    logging.info("Stopping Lifespan, Goodbye!")
app = FastAPI(lifespan=lifespan)

API_PREFIX = "/api"
app.include_router(user_router, prefix=API_PREFIX)
app.include_router(auth_router, prefix=API_PREFIX)
app.include_router(api_key_router, prefix=API_PREFIX)

if __name__ == "__main__":
    uvicorn.run(app)
