from abc import ABC, abstractmethod
import random

class Observable(ABC):
    @abstractmethod
    def add(self, *args, **kwargs):
        pass

    @abstractmethod
    def remove(self, *args, **kwargs):
        pass

    @abstractmethod
    def notify(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class WeatherStation:
    def __init__(self):
        self.observers = []
    
    def add(self, observer: Observer):
        self.observers.append(observer)
    
    def remove(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()
    
    def get_temperature(self):
        temperature = random.randint(0, 30)
        return temperature

class Phone:
    def __init__(self, observable: Observable) -> None:
        self.observable = observable
    
    def update(self):
        print(f"New temperature detected {self.observable.get_temperature()}")
    
class WindowDisplay:
    def __init__(self, observable: Observable) -> None:
        self.observable = observable
    
    def update(self):
        print(f"New temperature detected {self.observable.get_temperature()}")


station = WeatherStation()
phone = Phone(station)
window = WindowDisplay(station)
station.add(phone)
station.add(window)
station.notify()