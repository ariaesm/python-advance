# Python OOP — step by step

Short, runnable lessons on object-oriented programming in Python, from first classes to dunder methods. Each file is self-contained: read it top to bottom, then run it.

| # | Lesson | Covers |
| --- | --- | --- |
| 1 | [Classes and objects](oop/01_classes_and_objects.py) | `class`, `__init__`, attributes, methods |
| 2 | [Inheritance](oop/02_inheritance.py) | subclasses, `isinstance`, `__class__.__name__` |
| 3 | [Overriding and `super()`](oop/03_overriding_and_super.py) | replacing and extending parent methods |
| 4 | [Multiple inheritance](oop/04_multiple_inheritance.py) | combining parents, Method Resolution Order |
| 5 | [Dunder methods](oop/05_dunder_methods.py) | `__add__`, `__eq__`, `__repr__`, `@property`, `@dataclass` |

## Run

```bash
python oop/04_multiple_inheritance.py
# a crossover: high ground clearance, 5 seats
# Crossover -> OffRoader -> PassengerCar -> object
```

## Tests

Every lesson is executed by the test suite, plus a few checks on the classes:

```bash
pip install pytest
pytest
```

## License

[MIT](LICENSE)
