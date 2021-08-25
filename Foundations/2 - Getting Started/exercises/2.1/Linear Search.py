def linear_search(A, key):
    # for i = 0 to A.length-1
    for i in range(len(A)):
        # compare each item with the key
        if A[i] == key:
            # if there is a match then return the index of item in array
            return i
    # no match found return None
    return None


A = [31, 41, 59, 26, 41, 59, 58]

print(linear_search(A, key=41))

# you can observe the index of 1st match from left to right is returned
print(linear_search(A, key=59))

# When there is no match found
print(linear_search(A, key=3))
