from math import sqrt
from random import randint


def add(a, b):
    """function which implement summary

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: final result
    """
    return a + b


def multiply(a, b):
    """function which implement multiplication

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: final result
    """
    return a * b


def random_sqrt_sum():
    """function which implement summary of squared and randint 

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: final result
    """
    i = randint(1, 100)
    s = sqrt(i)
    return add(s, i)
