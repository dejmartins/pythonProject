def get_digit(number: int, position: int) -> int:
    """
    Get the digit at a particular position
    >>> get_digit(234, 0)
    4
    >>> get_digit(234,2)
    2
    >>> "hello"
    'hello'
    >>> '2' + 3 # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError:
    >>> x # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    NameError:
    """

    return number // (10 ** position) % 10


print(get_digit(234, 2))
