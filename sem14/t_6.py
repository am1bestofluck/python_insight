"""
На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры.
"""
import pytest

from sem13.t_5 import Auth, LevelException, AccessException


@pytest.fixture
def frame_a():
    return Auth()


@pytest.fixture
def frame_b():
    return Auth()


def test1(frame_a, frame_b):
    assert frame_a == frame_b


def test2(frame_a, frame_b):
    with pytest.raises(AccessException):
        frame_a.auth("no.", 1)


def test3(frame_a, frame_b):
    with pytest.raises(LevelException):
        frame_a.auth("A", 1)
        frame_a.add_user(("e", 1))


if __name__ == "__main__":
    pytest.main(['-v'])
