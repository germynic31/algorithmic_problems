from collections import Counter


def count_letters(text: str) -> dict:
    letter_count = Counter(
        [
            c for c in text.lower() if c.isalnum()
        ]
    )
    return dict(letter_count)


def test_count_letters():
    assert count_letters(
        'Hello world'
        ) == {
            'h': 1,
            'e': 1,
            'l': 3,
            'o': 2,
            'w': 1,
            'r': 1,
            'd': 1
            }
