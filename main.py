from fastapi import FastAPI
from h11 import Response
from pydantic import BaseModel

app = FastAPI()

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

@app.get("/cars/{car_id}")
def get_car_id(car_id: str, response: Response):
    for car in cars:
        if car.identifier == car_id:
            return car
    response.status_code = 404
    return {
        "error": "Voiture inexistante",
        "message": f"La voiture avec l'identifiant '{car_id}' n'existe pas"
    }
