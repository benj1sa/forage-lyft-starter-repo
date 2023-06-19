from tires.tires import Tires

class OctoPrimeTires(Tires):

    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self) -> bool:
        for i in self.tire_wear_sensors:
            if i > 0.9:
                return True
        return False