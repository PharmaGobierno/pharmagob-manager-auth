import uvicorn
from fastapi import FastAPI, status

from app.libs.logger_middleware import LoggerMiddleware
from app.v1.router import api_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(LoggerMiddleware)

    # Routers
    app.include_router(api_router, prefix="/v1")

    return app


app = create_app()


@app.get("/")
async def health_check():
    a = status.HTTP_200_OK
    return f"{a}, ready"


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
