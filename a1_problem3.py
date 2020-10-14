# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


from a1_include import *


def reverse(arr: StaticArray) -> None:
    """
    TODO: Write this implementation
    """
    return


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
