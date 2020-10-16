# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 1 Problem 5
# Description: Takes a range of numbers and outputs an array of that ranage


from a1_include import *


def sa_range(start: int, end: int) -> StaticArray:
    if end < start and end < 0: # checks if the end range is smaller than the start range for negative values
        empty = [_ for _ in range(abs(start), abs(end)+1)]  # create empty static array and use range to determine the size
        fb_arr = StaticArray(len(empty))  # call static array class to make new array
        for i, value in enumerate(empty):  # enumerate list and give it values
            fb_arr[i] = -value # adds a negative value to the array
        return fb_arr

    elif end > start and end < 0: # checks if the end range is larger than the start range
        empty = [_ for _ in range(abs(start), abs(end)-1, -1)]  # create empty static array and use range to determine length. Reverses the numbers
        fb_arr = StaticArray(len(empty))  # call static array class to make new array
        for i, value in enumerate(empty):  # enumerate list and give it values
            fb_arr[i] = -value # adds a negative value to the array
        return fb_arr

    elif end < start and end > 0:  # checks if the end range is larger than the start range
        empty = [_ for _ in range(abs(start), abs(end)-1, -1)]  # create empty static array and use range to determine length. Reverses the numbers
        fb_arr = StaticArray(len(empty))  # call static array class to make new array
        for i, value in enumerate(empty):  # enumerate list and give it values
            fb_arr[i] = value  # adds a negative value to the array
        return fb_arr

    else:
        empty = [_ for _ in range(start, abs(end)+1)]  # create empty static array and range for the size of the array
        fb_arr = StaticArray(len(empty))  # call static array class to make new array
        if end < 0: # checks if end is smaller than 0 for negative numbers
            for i, value in enumerate(empty):  # enumerate list and give it values
                fb_arr[i] = -value
        else:
            for i, value in enumerate(empty):  # enumerate list and give it values
                fb_arr[i] = value
        return fb_arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))
