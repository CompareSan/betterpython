from abc import ABC, abstractmethod

# Dependency inversion helps reduce coupling in your code
# Uses abstractions to separate classes
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class Fan(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class ElectricPowerSwitch:

    def __init__(self, client: Switchable):
        self.client = client
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


light_bulb = LightBulb()
fan = Fan()
switch = ElectricPowerSwitch(fan)
switch.press()
switch.press()