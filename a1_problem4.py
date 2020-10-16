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
    first_count = 1
    prev = 0
    counter = steps
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
