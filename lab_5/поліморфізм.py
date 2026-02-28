class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Fish(Animal):
    pass


if __name__ == "__main__":
    animals = [Dog(), Cat(), Fish()]

    for animal in animals:
        print(animal.speak())
        