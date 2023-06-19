from tires.tires import Tires

class CarriganTires(Tires):

    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self) -> bool:
        total_wear = 0
        for i in self.tire_wear_sensors:
            total_wear += i
        return total_wear >= 3
