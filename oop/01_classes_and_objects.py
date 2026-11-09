"""Lesson 1 — classes, objects, __init__ and instance attributes.

A class bundles data (attributes) with behaviour (methods). Every object
created from it gets its own copy of the attributes set in __init__.
"""


class Reverser:
    """Reverses whatever text it was created with."""

    def __init__(self, text: str) -> None:
        self.text = text

    def reversed(self) -> str:
        return self.text[::-1]


class Property:
    """A real-estate listing: commercial, office or residential."""

    def __init__(self, kind: str, built_in: int, area_m2: float, bedrooms: int = 0) -> None:
        self.kind = kind
        self.built_in = built_in
        self.area_m2 = area_m2
        self.bedrooms = bedrooms

    def describe(self) -> str:
        rooms = f", {self.bedrooms} bedroom(s)" if self.bedrooms else ""
        return f"{self.kind} property, {self.area_m2:g} m², built in {self.built_in}{rooms}"


if __name__ == "__main__":
    print(Reverser("12345").reversed())  # 54321
    home = Property("residential", 2020, 95, bedrooms=2)
    shop = Property("commercial", 2015, 40)
    print(home.describe())
    print(shop.describe())
