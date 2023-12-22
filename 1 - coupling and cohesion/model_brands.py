from abc import ABC, abstractmethod


class Brand(ABC):
    @abstractmethod
    def catalogue_price(self):
        pass

class TeslaModel3Brand(Brand):
    def catalogue_price(self):
        return 60000

class VolkswagenID3Brand(Brand):
    def catalogue_price(self):
        return 35000

class BMW5Brand(Brand):
    def catalogue_price(self):
        return 45000