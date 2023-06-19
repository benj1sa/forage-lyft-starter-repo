from datetime import date
from car import Cartire_wear_sensors
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBatter
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoPrimeTires

class CarFactory():

    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_sensors) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBatter(current_date, last_service_date)
        tires = CarriganTires(tire_wear_sensors)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_sensors) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBatter(current_date, last_service_date)
        tires = OctoPrimeTires(tire_wear_sensors)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tire_wear_sensors) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBatter(current_date, last_service_date)
        tires = CarriganTires(tire_wear_sensors)
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_sensors) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoPrimeTires(tire_wear_sensors)
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_sensors) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTires(tire_wear_sensors)
        return Car(engine, battery, tires)