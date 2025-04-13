import random


def quick_sort(a):
    len_a = len(a)

    if len_a <= 1:
        return a

    val = a[random.randint(0, len_a-1)]
    low = [n for n in a if n < val]
    mid = [n for n in a if n == val]
    high = [n for n in a if n > val]
    a = quick_sort(low) + mid + quick_sort(high)
    return a


if __name__ == '__main__':
    print(quick_sort(
        [9, 5, -3, -4, 7, 8, -8]
    ))
