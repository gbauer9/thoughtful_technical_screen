from ..package_sorting import _is_bulky, _is_heavy


def test_is_bulky_true_volume():
    assert _is_bulky(width=100, height=100, length=100) is True

def test_is_bulky_true_width():
    assert _is_bulky(width=150, height=1, length=1) is True

def test_is_bulky_true_height():
    assert _is_bulky(width=1, height=150, length=1) is True

def test_is_bulky_true_length():
    assert _is_bulky(width=1, height=1, length=150) is True

def test_is_bulky_false_volume():
    assert _is_bulky(width=99, height=100, length=100) is False

def test_is_bulky_false_width():
    assert _is_bulky(width=149, height=1, length=1) is False

def test_is_bulky_false_height():
    assert _is_bulky(width=1, height=149, length=1) is False

def test_is_bulky_false_length():
    assert _is_bulky(width=1, height=1, length=149) is False

def test_is_heavy_true():
    assert _is_heavy(mass=20) is True

def test_is_heavy_false():
    assert _is_heavy(mass=19) is False