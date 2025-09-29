import pytest
from car import Car
from track import Track

def test_car_drive_and_fuel():
    car = Car(7)   # 7л / 100 км
    car.fill_up(20)
    car.drive(100)   # расход 7л
    assert pytest.approx(car.remaining_fuel()) == 13

def test_car_not_enough_fuel():
    car = Car(7)
    car.fill_up(5)
    car.drive(200)   # нужно 14л, есть только 5
    assert car.remaining_fuel() == 0

def test_track_drive_and_fuel():
    track = Track(15, 2)  # 30л / 100 км
    track.fill_up(100)
    track.drive(100)  # расход 30л
    assert pytest.approx(track.remaining_fuel()) == 70

def test_track_not_enough_fuel():
    track = Track(15, 2)
    track.fill_up(10)
    track.drive(100)  # нужно 30л
    assert track.remaining_fuel() == 0
