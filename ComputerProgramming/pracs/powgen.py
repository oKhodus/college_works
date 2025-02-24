def power_series(x: int|float):
    """Make the infinite power series of a given base x

    Args:
        x (int, float): The base value for the power series

    Yields:
        int, float: Powers of x (x^0, x^1, x^2, x^3, ... x^n)
    """
    n = 0
    while True:
        yield x**n
        n += 1


gen = power_series(5)
print([next(gen) for _ in range(5)])

"""
Testing modules - to test type [ pytest powgen.py ]
"""

def test_power():
    two = power_series(2)
    assert [next(two) for _ in range(5)] == [1, 2, 4, 8, 16]

    three = power_series(3)
    assert [next(three) for _ in range(5)] == [1, 3, 9, 27, 81]

    five = power_series(5)
    assert [next(five) for _ in range(5)] == [1, 5, 25, 125, 625]

    f_check = power_series(2.5)
    assert [next(f_check) for _ in range(4)] == [1.0, 2.5, 6.25, 15.625]