from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Profile(BaseModel):
    id: int
    name: str
    email: str

class HelloResponse(BaseModel):
    message: str

@app.get("/profile", response_model=Profile)
def profile():
    return Profile(id=1, name="Alice", email="alice@example.com")

@app.get("/hello/{name}", response_model=HelloResponse)
def hello(name: str):
    return HelloResponse(message=f"Hello {name}")
