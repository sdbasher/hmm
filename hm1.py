import time

class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print("max speed is", self.max_speed)


truck1 = Truck("Volvo", 3, "XC90", 5000, "black", 2500)
truck2 = Truck("Mercedes", 2, "Actros", 7000, "white")

print(truck1.brand)
print(truck1.age)
print(truck1.mark)
print(truck1.color)
print(truck1.weight)
print(truck1.max_load)

truck1.move()
truck1.load()
truck1.stop()
truck1.birthday()

print()

car1 = Car("Toyota", 1, "Camry", 200, "red", 1500)
car2 = Car("BMW", 2, "X5", 250, "blue")

print(car1.brand)
print(car1.age)
print(car1.mark)
print(car1.color)
print(car1.weight)
print(car1.max_speed)

car1.move()
car1.stop()
car1.birthday()
