# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 1 Problem 1
# Description:


from a1_include import *


def min_max(arr: StaticArray) -> ():
    """function takes the first integer on the static array and iterates through the entire list while comparing the
    previous value to the current position. If it's higher, it will take the place as the max integer. If it is lower,
    it will take the place as the min integer."""
    list_size = arr.size() # takes size of the array
    max_int = arr.get(index=0) # initiliaze index = 0 as the max
    min_int = max_int # set the max as min
    for i in range(list_size):
        if arr[i] > max_int:  # checks if the remaining integers is greater than first integer entered
            max_int = arr[i]
        if arr[i] < min_int:  # checks if the remaining integers is less than first integer entered
            min_int = arr[i]
    return min_int, max_int


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    arr = StaticArray(5)
    for i, value in enumerate([8, 7, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))

    # example 2
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))

    # example 3
    arr = StaticArray(3)
    for i, value in enumerate([3, 3, 3]):
        arr[i] = value
    print(min_max(arr))
