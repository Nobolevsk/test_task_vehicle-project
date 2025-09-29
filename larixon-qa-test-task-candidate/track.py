from vehicle import Vehicle

class Track(Vehicle):
    def __init__(self, consumption_per_trailer: float, trailers: int):
        self.consumption = consumption_per_trailer * trailers
        self.fuel = 0.0

    def fill_up(self, liters: int):
        self.fuel += liters

    def drive(self, distance: float):
        required = (distance / 100.0) * self.consumption
        if required > self.fuel:
            self.fuel = 0.0
        else:
            self.fuel -= required

    def remaining_fuel(self) -> float:
        return self.fuel
