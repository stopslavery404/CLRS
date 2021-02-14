def insertion_sort(array):
    """Program for insertion sort
    Inplace sorting
    Space Complexity O(1)   only constant number of variables is used
    Time complexity O(n^2)
    >>> arr = [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
    >>> print(arr)
    [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
    >>> insertion_sort(arr)
    >>> print(arr)
    [-3, 0, 0, 1, 1, 2, 5, 5, 7, 9]
    """

    for j in range(1, len(array)):
        key = array[j]
        # Insert array[j] into the sorted sequence array[0.. j-1]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key


arr = [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
print(arr)
insertion_sort(arr)
print(arr)
