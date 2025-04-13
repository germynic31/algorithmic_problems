from list_merging_method import list_merging_method


def split_and_merge_list(arr):
    len_arr = len(arr) // 2
    lis1 = arr[:len_arr]
    lis2 = arr[len_arr:]
    if len(lis1) > 1:
        lis1 = split_and_merge_list(lis1)
    if len(lis2) > 1:
        lis2 = split_and_merge_list(lis2)

    return list_merging_method(lis1, lis2)


if __name__ == '__main__':
    print(split_and_merge_list(
        [9, 5, -3, 4, 7, 8, -8]
    ))
