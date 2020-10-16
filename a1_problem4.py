# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


from a1_include import *


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    empty = [_ for _ in range(arr.size())] # create empty static array and use size of current array as length
    fb_arr = StaticArray(len(empty)) # call static array class to make new array
    for i, value in enumerate(empty): # enumerate list and give it values
        fb_arr[i] = value
    for i in range(arr.size()): # iterate through current array and copy the contents over
        fb_arr[i] = arr[i]
    for index in range(fb_arr.size()): # iterate through new array


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        print(rotate(arr, steps), steps)
    print(arr)
