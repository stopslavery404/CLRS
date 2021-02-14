def linear_search(array, item):
    """Returns true if item is in array
    Time Complexity O(n)
    """
    for i in range(len(array)):
        if array[i] == item:
            return True
    return False


def linear_search_1(array, item):
    """Returns position of item in array if item is found in array
    else returns length(array).
    Time Complexity O(n)
    """
    for i in range(len(array)):
        if array[i] == item:
            return i
    return len(array)

i=linear_search_1([1,2,3,4,5],8)
print(i)