from src.main import index, add
import pytest


def test_index():
    assert index() == "Hello, world!"


@pytest.mark.parametrize('x, y, result', [
    (10, 10, 20),
    (5, 5, 10),
    (6, 6, 12)
])
def test_add(x, y, result):
    assert add(x, y) == result
