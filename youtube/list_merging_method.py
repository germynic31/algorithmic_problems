def list_merging_method(arr1, arr2):
    sorted_array = []

    len_arr1 = len(arr1)
    len_arr2 = len(arr2)

    i = 0
    j = 0
    while i < len_arr1 and j < len_arr2:
        if arr1[i] <= arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        else:
            sorted_array.append(arr2[j])
            j += 1

    sorted_array += arr1[i:] + arr2[j:]
    return sorted_array


if __name__ == '__main__':
    print(list_merging_method(
        [1, 4, 10, 11],
        [2, 3, 3, 4, 8]
    ))
