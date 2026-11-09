"""Lesson 2 — inheritance.

A subclass gets every method of its parent and can add its own.
self.__class__.__name__ shows which concrete class is running the method.
"""


class Animal:
    def walk(self) -> str:
        return f"{self.__class__.__name__}: walking..."

    def breathe(self) -> str:
        return f"{self.__class__.__name__}: breathing..."


class Sparrow(Animal):
    def fly(self) -> str:
        return f"{self.__class__.__name__}: flying..."


class Dog(Animal):
    def run(self) -> str:
        return f"{self.__class__.__name__}: running..."


if __name__ == "__main__":
    sparrow, dog = Sparrow(), Dog()
    for line in (sparrow.walk(), sparrow.breathe(), sparrow.fly(), dog.walk(), dog.run()):
        print(line)
    print(isinstance(dog, Animal))  # True — a Dog *is an* Animal
