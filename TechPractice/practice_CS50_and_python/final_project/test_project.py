from project import academic_year
from project import check_standard
from project import Register

def test_academic_year():
    assert academic_year() == "Academic_year_2022-23"

def test_checkStandard():
    # if user type in 2
    assert check_standard() == 2
    # if user type in 5
    assert check_standard() == 5

def test_registerClass():
    reg = Register(3, "Academic_year_2022-23")
    assert reg.STD == 3
    assert reg.Ayear == "Academic_year_2022-23"

# not able to test file saving and reading
# we can run this program it is working fine already tested practically