# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 1 Problem 6
# Description: Takes a static array and checks if array is in ascending or descending order. Return 1 for ascending,
# return 2 for descending, and return 0 if neither.


from a1_include import *


def is_sorted(arr: StaticArray) -> int:
    if arr.size() == 1: # if array has one element. Return 1
        return 1
    for index in range(arr.size() - 1): # iterate through array
        if arr[index] == arr[index + 1]: # if array only has two elements and they both equal each other, return 0
            return 0
        if arr[index] < arr[index + 1]: # checks if array is in ascending order
            wrong = 0 # wrong flag is initialized
            place = 1 # initialize the second index
            while place < arr.size():
                if arr[place] <= arr[place-1]: # if the previous index is smaller, the wrong flag is triggered
                    wrong = 1
                place += 1 # if not, keep moving forward
            if not wrong:
                return 1 # if not triggered, return 1
            else:
                return 0 # if triggered, return 0
        if arr[index] > arr[index + 1]: # checks for descending order
            wrong = 0 # wrong flag is set as 0
            place = 1 # initialize the second index
            while place < arr.size():
                if arr[place] >= arr[place - 1]: # if the previous index is bigger, the wrong flag is triggered
                    wrong = 1
                place += 1 # if not, keep moving forward
            if not wrong:
                return 2 # if not triggered, return 2
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
        [1, 3],
        [0, 0]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)
