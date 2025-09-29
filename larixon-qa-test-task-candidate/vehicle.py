from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fill_up(self, liters: int):
        pass

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def remaining_fuel(self) -> float:
        pass 