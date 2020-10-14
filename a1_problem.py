# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


from a1_include import *


def min_max(arr: StaticArray) -> ():
    """
    TODO: Write this implementation
    """
    return 0, 0


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
