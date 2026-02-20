class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def __repr__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.price} SEK"

    def __add__(self, other):
        if isinstance(other, Car):
            return self.price + other.price


class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, brand, model, year, price):
        car = Car(brand, model, year, price)
        self.cars.append(car)

    def total_cost(self):
        car_costs = []
        for car in self.cars:
            car_costs.append(car.price)
        return sum(car_costs)
