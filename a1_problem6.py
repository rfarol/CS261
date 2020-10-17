# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


from a1_include import *


def is_sorted(arr: StaticArray) -> int:
    if arr.size() == 1:
        return 1
    for index in range(arr.size() - 1): # iterate through array
        if arr[index] < arr[index + 1]:
            flag = 0
            i = 1
            while i < arr.size():
                if arr[i] <= arr[i-1]:
                    flag = 1
                i += 1
            if not flag:
                return 1
            else:
                return 0
        if arr[index] > arr[index + 1]:
            flag = 0
            i = 1
            while i < arr.size():
                if arr[i] >= arr[i - 1]:
                    flag = 1
                i += 1
            if not flag:
                return 2
            else:
                return 0







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
        ['apple'],
        [1, 3]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)
