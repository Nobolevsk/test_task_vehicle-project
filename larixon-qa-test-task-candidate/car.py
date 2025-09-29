from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, consumption_per_100km: float):
        self.consumption = consumption_per_100km
        self.fuel = 0.0

    def fill_up(self, liters: int):
        self.fuel += liters

    def drive(self, distance: float):
        required = (distance / 100.0) * self.consumption
        if required > self.fuel:
            # едем только на то, что есть
            self.fuel = 0.0
        else:
            self.fuel -= required

    def remaining_fuel(self) -> float:
        return self.fuel
