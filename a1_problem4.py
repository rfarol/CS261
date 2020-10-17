# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


from a1_include import *


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    empty = [_ for _ in range(arr.size())]  # create empty static array and use size of current array as length
    fb_arr = StaticArray(len(empty))  # call static array class to make new array
    for i, value in enumerate(empty):  # enumerate list and give it values
        fb_arr[i] = value
    index1 = 0
    index2 = 0
    if steps > 0:
        move = (fb_arr.size()-1) % steps
        arr[index1] = fb_arr[index2 + move]
    return fb_arr








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
