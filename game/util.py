from math import *


def get_angle(pos1, pos2):
    """
    Get the angle between 2 points

    Arguments:
        pos1 {tuple} -- position of 1st object
        pos2 {tuple} -- position of 2nd object
    """

    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    return degrees(atan2(dy, dx))