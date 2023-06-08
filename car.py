from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = Engine()

    @abstractmethod
    def needs_service(self):
        pass
