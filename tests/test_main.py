import pytest

from main import fun


def test_main():
    actual = fun(.1)
    expected = .3
    assert actual == pytest.approx(expected), 'message'
    # assert actual == expected, 'message'
