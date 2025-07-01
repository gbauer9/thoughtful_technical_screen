from ..package_sorting import Stack, sort


def test_sort_standard():
    assert sort(width=99, height=100, length=100, mass=19) == Stack.STANDARD

def test_sort_special_heavy():
    assert sort(width=10, height=10, length=10, mass=20) == Stack.SPECIAL

def test_sort_special_bulky():
    assert sort(width=150, height=10, length=10, mass=10) == Stack.SPECIAL

def test_sort_rejected():
    assert sort(width=100, height=100, length=100, mass=20) == Stack.REJECTED