"""Lesson 3 — method overriding and super().

A subclass can replace a parent method (override) and still reuse the
parent's version through super().
"""


class Human:
    def say_hello(self) -> str:
        return "Hello from a human!"

    def ability(self) -> str:
        return "can walk and talk"


class Doctor(Human):
    def job(self) -> str:
        return "My job is doctor."

    def ability(self) -> str:
        return super().ability() + ", and can treat patients"


class Programmer(Human):
    def job(self) -> str:
        return "My job is programmer."

    def ability(self) -> str:
        return super().ability() + ", and can write software"


class Bird:
    def flying(self) -> str:
        return "most birds can fly"


class Chicken(Bird):
    def flying(self) -> str:  # override: chickens are the exception
        return "chickens can only flutter a short distance"


if __name__ == "__main__":
    for person in (Human(), Doctor(), Programmer()):
        print(f"{type(person).__name__}: {person.ability()}")
    print(Chicken().flying())
