from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar2 = Jar(8)
    assert jar2.capacity == 8
    assert jar2.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(2)
    assert jar.size == 7


def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(2)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3

def test_error():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)
    with pytest.raises(ValueError):
        jar.withdraw(13)
    # jar2 = Jar(-1)
    # with pytest.raises(ValueError):
    #     jar2()