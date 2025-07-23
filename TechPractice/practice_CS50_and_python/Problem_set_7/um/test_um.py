from um import count

def test_um():
    assert count("um") == 1
    assert count("let the show") == 0
    assert count("Um, thanks for the album.") == 1

def test_um2():
    assert count("Um, thanks, um...") == 2