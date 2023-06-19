import unittest
from datetime import datetime

from engine.engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import Sternman_engine
from engine.willoughby_engine import Willoughby_engine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoPrimeTires

class TestEngine(unittest.TestCase):

    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    def test_capulet_engine_should_not_be_serviced(self):
        current_mileage = 25000
        last_service_mileage = 20000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_sternman_engine_should_be_serviced(self):
        engine = Sternman_engine(True)
        self.assertTrue(engine.needs_service())
    def test_sternman_engine_should_not_be_serviced(self):
        engine = Sternman_engine(False)
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = Willoughby_engine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    def test_willoughby_engine_should_not_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 60000
        engine = Willoughby_engine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

class TestBattery(unittest.TestCase):

    def test_nubbin_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
    def test_nubbin_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 4)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
    def test_spindler_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

class TestTires (unittest.TestCase):

    def test_carrigan_tires_should_be_serviced(self):
        tire_wear_sensors = [0,0,0,1]
        tires = CarriganTires(tire_wear_sensors)
        self.assertTrue(tires.needs_service())
        
    def test_carrigan_tires_should_not_be_serviced(self):
        tire_wear_sensors = [0,0,0,0]
        tires = CarriganTires(tire_wear_sensors)
        self.assertFalse(tires.needs_service())

    def test_carrigan_tires_should_be_serviced(self):
        tire_wear_sensors = [1,1,1,1]
        tires = OctoPrimeTires(tire_wear_sensors)
        self.assertTrue(tires.needs_service())
    def test_carrigan_tires_should_not_be_serviced(self):
        tire_wear_sensors = [0,0,0,1]
        tires = OctoPrimeTires(tire_wear_sensors)
        self.assertFalse(tires.needs_service())
    

if __name__ == '__main__':
    unittest.main()