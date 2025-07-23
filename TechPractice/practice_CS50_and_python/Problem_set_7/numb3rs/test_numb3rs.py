from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
def test_value():
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False
    assert validate("512.1.1.1") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.512.1") == False
    assert validate("1.1.1.512") == False