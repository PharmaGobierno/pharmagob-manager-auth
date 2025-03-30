from infra.keycloak_auth import KeycloakAuthService

class AuthenticationController:
    """Controller for Authentication"""
    def __init__(self):
        self.keycloak_auth_service = KeycloakAuthService()

    def login(self, username: str, password: str) -> dict:
        """Login user and return access and refresh tokens."""
        return self.keycloak_auth_service.login(username, password)

    def refresh(self, refresh_token: str) -> dict:
        """Refresh access token using the refresh token."""
        return self.keycloak_auth_service.refresh(refresh_token)
