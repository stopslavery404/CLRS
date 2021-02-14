def merge_sort(arr, low, high):
    """Program for insertion sort
        Inplace sorting
        Space Complexity O(n)   a temporary array of linear size is used
        for each sub problem in merge setp
        Time complexity O(n log (n))
        >>> arr = [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
        >>> print(arr)
        [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
        >>> low=0
        >>> high = len(arr) - 1
        >>> merge_sort(arr, low, high)
        >>> print(arr)
        [-3, 0, 0, 1, 1, 2, 5, 5, 7, 9]
        """

    if low < high:
        mid = (low + high) // 2

        merge_sort(arr, low, mid)  # Recursively sort first half
        merge_sort(arr, mid + 1, high)  # Recursively sort second half
        merge(arr, low, mid, high)  # merge the two already sorted subarrays


def merge(arr, low, mid, high):
    L = arr[low:mid + 1]
    R = arr[mid + 1:high + 1]
    L.append(float('inf'))
    R.append(float('inf'))
    i = j = 0
    for k in range(low, high + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


'''    
# Simpler implementation for python

def merge_sort(array):
    """Program for insertion sort
    Inplace sorting
    Space Complexity O(n)   a temporary array of linear size is used
    for each sub problem in merge setp
    Time complexity O(n log (n))
    >>> arr = [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
    >>> print(arr)
    [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
    >>> merge_sort(arr)
    >>> print(arr)
    [-3, 0, 0, 1, 1, 2, 5, 5, 7, 9]
    """

    def merge_sort_util(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = merge_sort_util(arr[:mid])
            R = merge_sort_util(arr[mid:])
            return merge(L, R)
        return arr

    def merge(arr1=[], arr2=[]):
        i = 0
        j = 0
        result = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        result.extend(arr1[i:])
        result.extend(arr2[j:])
        return result

    arr[:] = merge_sort_util(array)

'''
arr = [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
