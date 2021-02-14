def selection_sort(array):
    """Program for selection sort
    Inplace sorting
    Space Complexity O(1)   only constant number of variables is used
    Time complexity O(n^2)
    >>> arr = [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
    >>> print(arr)
    [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
    >>> selection_sort(arr)
    >>> print(arr)
    [-3, 0, 0, 1, 1, 2, 5, 5, 7, 9]
    """

    n = len(array)
    for i in range(n - 1):
        minimum = array[i]
        min_index = i
        # find the minimum element in array[i+1..n-1]
        for j in range(i + 1, n):
            if array[j] < minimum:
                minimum = array[j]
                min_index = j
        # swap array[i] with minimum element found after i
        array[i], array[min_index] = array[min_index], array[i]


arr = [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
print(arr)
selection_sort(arr)
print(arr)
