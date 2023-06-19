from servicable import Servicable

class Car(Servicable):
    
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or tires.needs_service()
