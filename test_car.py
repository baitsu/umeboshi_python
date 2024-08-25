import pytest
import car

def test_car():
    test = car.Car()
    assert test.fell == 10
    assert test.efficiency == 40

def test_car_401():
    test = car.Car()
    assert test.drive(401) == 400
    assert test.drive(1) == 0
    

def test_car_def():
    test = car.Car()
    assert test.drive(100) == 100
    assert test.drive(0) == 0
    assert test.drive(-100) == -100
