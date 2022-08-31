from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers.routers import router
from core.db import db

app = FastAPI()

app.include_router(router, tags=['appointment'])


origins = [
        "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
