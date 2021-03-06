"""Provide several sample math calcs.

This module allows the user to make mathematicl calculations.

The module contains teh following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.

"""


from typing import Union

def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    """
    return float (a + b)


def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the difference of two numbers.

    Examples:

        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    """
    return float (a - b)


def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """ Compute and return the product of two numbers.

    Examples:

        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    """
    return float(a * b)


def divide(a: float | int, b: float | int) -> float:
    """Compute and return the quotient of two numbers.

    Examples:

        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0
        >>> divide(4, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: Isn't possible divide by zero

    Raises:
        ZeroDivisionError: An error occurs when the divisor is `0`.


    """
    if b == 0:
        raise ZeroDivisionError("Isn't possible divide by zero")
    return float(a / b)


