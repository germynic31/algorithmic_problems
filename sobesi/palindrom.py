# input_str = "A man, a plan, a canal: Panama"
# Решение: True (очищенная строка "amanaplanacanalpanama" — палиндром)


def is_palidrom(string: str):
    s = ''.join([
        c for c in string.lower() if c.isalnum()
    ])
    return s == s[::-1]


def test_is_palidrom():
    result = is_palidrom("A man, a plan, a canal: Panama")
    assert result is True
