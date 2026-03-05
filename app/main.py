from fastapi import FastAPI
from .database import Base, engine
from .routes import employees
from .auth import create_token

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management REST API")

@app.post("/token")
def login():
    return {"access_token": create_token(), "token_type": "bearer"}

app.include_router(employees.router)
