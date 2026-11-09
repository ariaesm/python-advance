"""Lesson 4 — multiple inheritance and the MRO.

A crossover car is both a high-clearance off-roader and a passenger car,
so it inherits from both. Python resolves methods with the Method
Resolution Order (MRO), shown by Crossover.__mro__.
"""


class OffRoader:
    def ground_clearance(self) -> str:
        return "high ground clearance"

    def describe(self) -> str:
        return "built for rough roads"


class PassengerCar:
    def seats(self) -> int:
        return 5

    def describe(self) -> str:
        return "built for comfort"


class Crossover(OffRoader, PassengerCar):
    def describe(self) -> str:
        return f"a crossover: {self.ground_clearance()}, {self.seats()} seats"


if __name__ == "__main__":
    car = Crossover()
    print(car.describe())
    print(" -> ".join(cls.__name__ for cls in Crossover.__mro__))
    # Crossover -> OffRoader -> PassengerCar -> object
