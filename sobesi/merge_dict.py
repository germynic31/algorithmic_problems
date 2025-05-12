from collections import Counter


def merge_dicts(dict1: dict, dict2):
    result = Counter(
        dict1
    )
    result.update(dict2)
    return dict(result)


def test_merge_dicts():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    result = merge_dicts(dict1, dict2)
    assert result == {'a': 1, 'b': 5, 'c': 4}, result


test_merge_dicts()
