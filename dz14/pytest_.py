import pytest

from dz13.t_3_Person import Person, InvalidNumberError
from dz13.t_3_Specialist import Specialist, InvalidIdError


@pytest.fixture
def prs():
    return Person("A", "M", "F", 30)


@pytest.fixture
def emp():
    return Specialist(firname="A", lasname="M", fatname="F", age=30, id_=777777)


def test_1(prs, emp):
    assert str(prs) == "M A F, 30 лет."


def test_2(emp):
    with pytest.raises(InvalidIdError):
        emp.id_ = 1


def test_3(prs, emp):
    with pytest.raises(InvalidNumberError):
        prs.age = -1


if __name__ == '__main__':
    pytest.main(["-v"])
