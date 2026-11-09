import importlib.util
import pathlib
import runpy

import pytest

LESSONS = sorted(pathlib.Path(__file__).parent.joinpath("oop").glob("*.py"))


def load(name):
    path = next(p for p in LESSONS if p.stem.endswith(name))
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("path", LESSONS, ids=lambda p: p.name)
def test_every_lesson_runs(path, capsys):
    runpy.run_path(str(path), run_name="__main__")
    assert capsys.readouterr().out


def test_reverser():
    assert load("classes_and_objects").Reverser("abc").reversed() == "cba"


def test_super_extends_parent():
    m = load("overriding_and_super")
    assert m.Doctor().ability().startswith(m.Human().ability())


def test_mro_order():
    m = load("multiple_inheritance")
    assert [c.__name__ for c in m.Crossover.__mro__] == [
        "Crossover",
        "OffRoader",
        "PassengerCar",
        "object",
    ]


def test_money():
    m = load("dunder_methods")
    assert m.Money(1) + m.Money(2) == m.Money(3)
    with pytest.raises(ValueError):
        m.Money(1).amount = -5
