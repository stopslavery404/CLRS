def bubble_sort(array):
    """Program for bubble sort
    Inplace sorting
    Space Complexity O(1)   only constant number of variables is used
    Time complexity O(n^2)
    >>> arr = [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
    >>> print(arr)
    [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
    >>> bubble_sort(arr)
    >>> print(arr)
    [-3, 0, 0, 1, 1, 2, 5, 5, 7, 9]
    """

    for i in range(len(array) - 1):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                # Swap array[j] and array[j-1]
                array[j], array[j - 1] = array[j - 1], array[j]


arr = [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
print(arr)
bubble_sort(arr)
print(arr)

