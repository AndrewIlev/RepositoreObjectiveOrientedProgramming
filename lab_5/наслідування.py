class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"

    def start_engine(self):
        return f"{self.brand} {self.model} запускає двигун!"


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_info(self):
        return f"{super().display_info()}, Seats: {self.seats}"


# Тестування
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 5)
    print(car.display_info())
    print(car.start_engine())
    