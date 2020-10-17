# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 1 Problem 8
# Description: Takes the static array and removes the duplicates into a new array


from a1_include import *


def remove_duplicates(arr: StaticArray) -> StaticArray:
    fb_arr = StaticArray(arr.size()) # create new array
    counter = 0 # initialize it index at 0
    for i in range(0, arr.size()-1): # iterate all the elements on the current list
        if arr[i] != arr[i+1]: # if number is unique, store the elemnt into new array
            fb_arr[counter] = arr[i]
            counter += 1 # move counter
    fb_arr[counter] = arr[arr.size() - 1] # adds the last number onto the array
    counter += 1
    return fb_arr

# couldn't figure out how to adjust the array size for the new static array




# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)
