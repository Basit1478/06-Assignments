class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):       # Public method
        print(f"{self.brand} car started.")


# Usage
my_car = Car("Honda")
print(my_car.brand)
my_car.start()

