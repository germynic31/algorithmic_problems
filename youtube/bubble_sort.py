def bubble_sort(array):
    len_array = len(array)
    for i in range(0, len_array-1):
        for j in range(0, len_array-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


print(bubble_sort([7, 5, -8, 0, 10, 1]))
