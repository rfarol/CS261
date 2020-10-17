# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 1 Problem 4
# Description: Takes static array and returns a new static array with rotated steps


from a1_include import *


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    fb_arr = StaticArray(arr.size()) # call static array class to make new array
    first_count = 1 # current index
    prev = 0 # previous index
    counter = steps # step counter to move throughout list
    while counter != 0:
        if counter == 0:
            break
        else:
            for i in range(arr.size()):  # iterate through current array and copy the contents over
                if steps > 0:
                    fb_arr.set(first_count, arr.get(index=prev))
                    first_count = first_count + 1
                    prev = prev + 1
                    counter = counter - 1
                    if first_count == fb_arr.size():
                        first_count = 0
                    if prev == fb_arr.size():
                        prev = 0
                if steps < 0:
                    fb_arr.set(prev, arr.get(index=first_count)) # moves to the left (negative moves)
                    first_count = first_count + 1
                    prev = prev + 1
                    counter = counter - 1
                    if first_count == fb_arr.size():
                        first_count = 0
                    if prev == fb_arr.size():
                        prev = 0
            return fb_arr


# Ran out of time. I could only move it one step to the right and left. lace the first index value of the original array into the
# second index of the new array. Then set up a loop counter for the number of steps so the array continuosly moves.
# Once the index hits the end of the array, it resets to 0 and goes back the front.

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
