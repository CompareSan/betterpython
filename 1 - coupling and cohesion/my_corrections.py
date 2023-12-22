import string
import random
from abc import ABC, abstractmethod
from model_brands import Brand, TeslaModel3Brand, VolkswagenID3Brand, BMW5Brand

class BaseRegistry(ABC):
    @abstractmethod
    def generate_vehicle_id(self, *args, **kwargs):
        pass

    @abstractmethod
    def generate_vehicle_license(self, *args, **kwargs):
        pass

class VehicleRegistry(BaseRegistry):

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

class Application:

    def register_vehicle(self, registry: BaseRegistry):
        
        # generate a vehicle id of length 12
        self.vehicle_id = registry.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        self.license_plate = registry.generate_vehicle_license(self.vehicle_id)
    
    @staticmethod
    def compute_catalog_price(brand: Brand):
        return brand.catalogue_price()

    @staticmethod
    def compute_tax_percentage(brand: Brand):
        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * Application.compute_catalog_price(brand)
        return payable_tax

    def get_info_vehicle_registration(self, registry: BaseRegistry, brand: Brand):
        # print out the vehicle registration information
        self.register_vehicle(registry)
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {self.vehicle_id}")
        print(f"License plate: {self.license_plate}")
        print(f"Payable tax: {self.compute_tax_percentage(brand)}")

app = Application()
registry = VehicleRegistry()
app.get_info_vehicle_registration(registry, TeslaModel3Brand())
