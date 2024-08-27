from pydantic import BaseModel

class SignupRequest(BaseModel):
    name: str
    email: str
    password: str

class SignupResponse(BaseModel):
    id: str
    name: str
    token: str

class SigninRequest(BaseModel):
    email: str
    password: str

class SigninResponse(BaseModel):
    id: str
    name: str
    token: str
