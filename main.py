from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def ping():
    return {"ping": "pong"}

class Characteristic(BaseModel):
    max_speed: float
    max_fuel_capacity: float

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic
cars = []

@app.get("/ping")
def ping():
    return "pong"

@app.post("/cars", status_code=201)
def create_cars(new_cars: list[Car]):
    cars.extend(new_cars)
    return {
        "message": f"{len(new_cars)} voiture ajouté",
        "total": len(cars)
    }

@app.get("/cars")
def get_cars():
    return cars