from infra.keycloak_auth import KeycloakAuthService
from keycloak.exceptions import KeycloakAuthenticationError, KeycloakPostError
from utils.logger import Logger
from app.v1.exceptions.errors import LoginError
from presentation.errors import ErrorLocationEnum


from ._base import BaseController


class AuthenticationController(BaseController):
    """Controller for Authentication"""

    def __init__(self, *, logger: Logger, verbose: bool = True) -> None:
        self.keycloak_auth_service = KeycloakAuthService()
        super().__init__(logger=logger, verbose=verbose)

    def login(self, username: str, password: str) -> dict:
        """Login user and return access and refresh tokens."""
        try:
            return self.keycloak_auth_service.login(username, password)
        except KeycloakAuthenticationError as e:
            if e.response_code == 401:
                self.logger.log_error(f"Invalid user credentials: {e}")
                raise LoginError(
                    location=ErrorLocationEnum.BODY,
                    parameter="credentials",
                    details="Invalid user credentials."
                )
            else:
                raise

    def refresh(self, refresh_token: str) -> dict:
        """Refresh access token using the refresh token."""
        try:
            return self.keycloak_auth_service.refresh_token(refresh_token)
        except KeycloakPostError as e:
            self.logger.log_error(f"Token is not active: {e}")
            raise LoginError(
                location=ErrorLocationEnum.BODY,
                parameter="credentials",
                details="Token is not active."
            )
