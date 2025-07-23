from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"

def test_vowels():
    assert shorten("onlyAEIOUaeiou") == "nly"