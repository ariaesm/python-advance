"""Lesson 5 — special ("dunder") methods, properties and dataclasses."""

from dataclasses import dataclass


class Money:
    def __init__(self, amount: float, currency: str = "USD") -> None:
        self._amount = amount
        self.currency = currency

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, value: float) -> None:
        if value < 0:
            raise ValueError("amount cannot be negative")
        self._amount = value

    def __add__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Money) and (self.amount, self.currency) == (
            other.amount,
            other.currency,
        )

    def __repr__(self) -> str:
        return f"Money({self.amount:g}, {self.currency!r})"


@dataclass(frozen=True)
class Point:
    """dataclass writes __init__, __repr__ and __eq__ for us."""

    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


if __name__ == "__main__":
    print(Money(10) + Money(5.5))  # Money(15.5, 'USD')
    print(Point(0, 0).distance_to(Point(3, 4)))  # 5.0
