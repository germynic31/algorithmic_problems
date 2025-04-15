# Write a function which calculates the average of the numbers in a given array.

# Note: Empty arrays should return 0.


def find_average(numbers):
    if not numbers:
        return 0
    current_number = 0
    for number in numbers:
        current_number += number
    return current_number / len(numbers)


def find_average2(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
