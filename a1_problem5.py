# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


from a1_include import *


def sa_range(start: int, end: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    return StaticArray()


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))
