class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"Driving {self.brand}")

car = Car("Toyota")

car.drive()