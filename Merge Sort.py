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
        if len(arr)>1:
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

    arr[:]=merge_sort_util(array)


arr = [1, 5, 0, -3, 5, 7, 2, 0, 9, 1]
print(arr)
merge_sort(arr)
print(arr)
merge_sort(arr)
