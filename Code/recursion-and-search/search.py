#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # Found
    return None  # Not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if index > len(array) - 1:
        return None
    if item == array[index]:
        return index

    # If doesn't satisfy base case, calls function again but index goes up one
    else:
        return linear_search_recursive(array, item, index+1) 

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    left = 0
    right = len(array) - 1

    while right >= left:
        middle = (right + left) // 2
        if item > array[middle]: # Shift the left if item is greater than middle of array
            left = middle + 1
        elif item < array[middle]:
            right = middle - 1
        else:
            return middle

    return None


def binary_search_recursive(array, item, left=None, right=None):
#     # TODO: implement binary search recursively here
#     # once implemented, change binary_search to call binary_search_recursive
#     # to verify that your recursive implementation passes all tests

    if left == None:
        left = 0
        right = len(array) - 1

    middle = (left + right) // 2

    # Base cases
    if right < left:
        return None
    elif array[middle] == item:
        return middle

    # Call function if recursively if doesn't satisfy base case
    # The left or right is shifted based on if the item is lower or higher than array[middle]
    if array[middle] < item:
        return binary_search_recursive(array, item, left=middle+1, right=right)
    else:
        return binary_search_recursive(array, item, left=left, right=middle-1)