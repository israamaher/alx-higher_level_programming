#!/usr/bin/paython3
""" add_integer method """
def add_integer(a, b=98):
    """
    add two integer.
    Arg:
        a : the first integer
        b : the secand integer
    Raise:
        TypeErrore
    return 
        the sum of two integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
