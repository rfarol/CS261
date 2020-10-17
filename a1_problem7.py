# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 1 Problem 7
# Description: Sorts array in ascending order


from a1_include import *


def sa_sort(arr: StaticArray) -> None:
    for index in range(arr.size()): # iterate through array
        for index_2 in range(index + 1, arr.size()): # nested loop to check iteration. increment by 1
            if arr[index] > arr[index_2]: # checks current index is larger than the next increment
                temp = arr[index] # stores current index value in variable
                arr[index] = arr[index_2] # next increment takes over current index value
                arr[index_2] = temp # current index value moves forward along the array
    return



# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        sa_sort(arr)
        print(arr)
