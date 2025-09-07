# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child Class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f" Calling {number} from {self.device_info()}...")

    def charge(self, amount):
        self.battery += amount
        print(f" Battery charged to {self.battery}%")

    def __str__(self):
        return f"Smartphone: {self.device_info()}, Storage: {self.storage}GB, Battery: {self.battery}%"

# Create Objects
phone1 = Smartphone("Apple", "iPhone 14", 128, 50)
phone2 = Smartphone("Samsung", "Galaxy S23", 256, 75)

print(phone1)
phone1.make_call("0712345678")
phone1.charge(30)

print(phone2)
phone2.make_call("0798765432")
