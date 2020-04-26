import sys
sys.path.append("..")
from game.util import get_angle


def test_get_angle():
    assert get_angle((10, 10), (50, 50)) == -135
    assert get_angle((50, 50), (10, 10)) == 45

    assert get_angle((0, 100), (100, 100)) == 180
    assert get_angle((100, 100), (0, 100)) == 0