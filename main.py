import os

import uvicorn
from fastapi import FastAPI, status

from app.libs.logger_middleware import LoggerMiddleware
from fastapi.middleware.cors import CORSMiddleware
from app.v1.router import api_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(LoggerMiddleware)
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type"],
    allow_credentials=True,
    max_age=600,
)

    # Routers
    app.include_router(api_router, prefix="/v1")
    return app


app = create_app()


@app.get("/")
async def health_check():
    a = status.HTTP_200_OK
    return f"{a}, OK"


if __name__ == "__main__":
    uvicorn.run(app, port=int(os.environ.get("PORT", 8080)), host="0.0.0.0")
