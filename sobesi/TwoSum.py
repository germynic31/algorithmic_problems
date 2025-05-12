# nums = [2, 7, 11, 15], target = 9


def two_sum(nums: list[int], target: int):
    num_index_dict = dict()
    for i, num in enumerate(nums):
        result = target - num
        if result in num_index_dict:
            return [num_index_dict[result], i]
        num_index_dict[num] = i
    return []


def test_two_sum():
    result = two_sum([2, 7, 11, 15], 9)
    assert result == [0, 1], result


test_two_sum()
