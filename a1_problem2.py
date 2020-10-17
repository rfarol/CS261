# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 1 Problem 2
# Description: Creates a new static array and checks if the numbers are divisible by 3, 5, or both. If they are
# divisible by those numbers, they are replaced with fizz, buzz, or fizzbuzz respectively.


from a1_include import *


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """create new array and checks for numbers divisible by 3, 5, or both. Replaces it with fizz, buzz, or fizzbuzz"""
    fb_arr = StaticArray(arr.size()) # call static array class to make new array
    for i in range(arr.size()): # iterate through current array and copy the contents over
        fb_arr[i] = arr[i]
    for index in range(fb_arr.size()): # iterate through new array and check for divisibility
        if fb_arr[index] % 3 == 0 and fb_arr[index] % 5 == 0:
            fb_arr[index] = "fizzbuzz" # if both divisible by 3 and 5, replace with fizzbuzz
        elif fb_arr[index] % 3 == 0:
            fb_arr[index] = "fizz" # if only divisible by 3, replace with fizz
        elif fb_arr[index] % 5 == 0:
            fb_arr[index] = "buzz" # if only divisible by 5, replace with buzz
    return fb_arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)
