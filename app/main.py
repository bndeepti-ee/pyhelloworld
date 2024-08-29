from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World"


@app.get("/hello/{where}")
def read_from(where: str):
    return (f"Hello from {where.capitalize()} World")