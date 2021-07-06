# File name: Search_Algorithms.py
# Description: File of functions containing common search algorithms


def linearSearch(array, searchVal):
    for index in array:
        if index == searchVal:
            return True

    return False


def binarySearch(array, startIndex, endIndex, searchVal):
    # recursion method of a binary search

    # check a base case
    if endIndex >= startIndex:

        # find midpt of array
        midpt = startIndex + (endIndex-startIndex)/2

        # return searchval if it is in the middle
        if array[midpt] == searchVal:
            return midpt

        # search left half array
        elif array[midpt] > searchVal:
            return binarySearch(array, startIndex, midpt-1, searchVal)

        # search right half of array
        else:
            return binarySearch(array, midpt+1, endIndex, searchVal)
    else:
        # searchval inst found and returns a negative one stating false
        return -1
