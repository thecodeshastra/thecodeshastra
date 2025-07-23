from seasons import convert
import pytest

def test_val():
    assert convert("2023-03-14") == "One thousand, four hundred forty"
    assert convert("2023-03-14") == "One thousand, four hundred forty"

def test_error():
    with pytest.raises(SystemExit):
        convert("23-01-13")