#!/usr/bin/python3

"""Finds a peak element in unsorted list using binary search."""


def find_peak(nums):
    """Finds a peak element
    args:
        nums: list of unsorted integers
    """

    low = 0
    length = len(nums)
    h = length - 1
    m = h // 2

    if nums is None or length == 0:
        return None

    while low <= h:
        mid = nums[m]
        if ((m == 0 or mid > nums[m - 1]) and
                (m == length - 1 or mid > nums[m + 1])):
            return mid
        elif mid < nums[m + 1]:
            low = m + 1
            m = (h + low) // 2
        else:
            h = m - 1
            m = (h + low) // 2

    return mid
