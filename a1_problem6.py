# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


from a1_include import *


def is_sorted(arr: StaticArray) -> int:
    if arr.size() == 1:
        return 0
    for index in range(arr.size() - 1): # iterate through array
        if arr[index] > arr[index + 1] and arr[index + 1] >= arr[index + 2] and arr[index + 2] <= arr[index + 3]:
            return 0
        elif arr[index] > arr [index + 1]:
            return 2
        elif arr[index] < arr[index + 1] and arr[index + 1] >= arr[index + 2] and arr[index + 2] <= arr[index + 3]:
            return 0
        elif arr[index] < arr[index + 1]:
            return 1





# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '1'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)
