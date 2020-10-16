# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 1 Problem 3
# Description: Takes an array and reverses the order using a while loop


from a1_include import *


def reverse(arr: StaticArray) -> None:
    """takes array and move the first indexed number to the end and last indexed number to the front, then move
    throughout the list"""
    loop_count = arr.size()/2 # loop counter
    last_count = arr.size() - 1 # initialize the last index
    first_count = 0 # initialize the first index
    temp = 0 # filler variable to store value
    while loop_count != 0: # set loop counter to keep going until full array is iterated
        if arr.get(index=first_count) != arr.get(index=last_count): # this is to ensure if same numbers are in array
            temp = arr.get(index=first_count) # put first index value in variable to store
            arr.set(first_count, arr.get(index=last_count)) # move the last indexed variable to the beginning of the array
            arr.set(last_count, temp) # move the first indexed variable to the end of the array
            first_count = first_count + 1 # move through the list from the front
            last_count = last_count - 1 # move through the list from the back
            loop_count = loop_count - 1 # move loop counter down
        else:
            return
    return arr





# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)
