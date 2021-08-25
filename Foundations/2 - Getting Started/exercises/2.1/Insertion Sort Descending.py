# Function for Insertion sort in descending order
def insertion_sort_descending(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


# Input array
A = [31, 41, 59, 26, 41, 58]
print(A)
insertion_sort_descending(A)

# Array after sorting
print(A)
