"""
* :description: Schema
"""

from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    password: str
    


class RefreshSchema(BaseModel):
    refresh: str
