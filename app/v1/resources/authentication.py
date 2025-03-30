"""
* :description: Namespace for Authentication
"""

from fastapi import APIRouter, Request, Response, status

from app.v1.controllers.authentication import AuthenticationController
from app.v1.exceptions.handler import exception_handler
from app.v1.schemas.authentication import LoginSchema, RefreshSchema

router = APIRouter()


# ? [POST] <— /v1/token
@router.post("")
@exception_handler(response_status=status.HTTP_200_OK)
async def post_token(
    request: Request,
    response: Response,
) -> dict:
    """Endpoint ..."""
    controller_input: LoginSchema = LoginSchema.model_validate(await request.json())
    controller = AuthenticationController()
    return controller.login(
        controller_input.username,
        controller_input.password,
    )


# ? [POST] <— /v1/token/refresh
@router.post("/refresh")
@exception_handler(response_status=status.HTTP_200_OK)
async def post_refresh(
    request: Request,
    response: Response,
) -> dict:
    """Endpoint ..."""
    controller_input: RefreshSchema = RefreshSchema.model_validate(await request.json())
    controller = AuthenticationController()
    return controller.refresh(
        controller_input.refresh,
    )
