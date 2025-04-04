from presentation.errors import BaseError


class LoginError(BaseError):
    code: str = "UNAUTHORIZED"
    message: str = "Invalid user credentials."
    http_status = 401
