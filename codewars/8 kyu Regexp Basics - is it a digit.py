# Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a single digit (0-9), false otherwise.


import re


def is_digit(n):
    if n.isdigit() and len(n) == 1:
        return True
    return False
