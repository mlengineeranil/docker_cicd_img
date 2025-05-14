from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GreetRequest(BaseModel):
    name: str
    
    
@app.get("/")
def read_root():
    return {"message": "Hello From FastAPI in Docker!"}

#eighth commit
@app.post("/greet/{name}")
def greet_user(name : str):
    return {"message": f"Hello {name}!"}
    