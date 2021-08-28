# Exercise - 2.1

***1. Illustrate the operation of INSERTION-SORT on the array A = [31, 41, 59, 26, 41, 58]***

![img.png](img.png)


---

***2. Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order.***

_**Pseudo Code**_

```
insertion_sort_reverse(A)
    for j = 2 to A.length
        key = A[j]
        // Insert A[j] into sorted sequence A[1 .. j-1]
        i = j-1
        while i > 0 and A[i] < key
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
```

[Java](https://github.com/pctablet505/CLRS/blob/master/Foundations/2%20-%20Getting%20Started/exercises/2.1/java/InsertionSortDescending.java)

[Python](https://github.com/pctablet505/CLRS/blob/master/Foundations/2%20-%20Getting%20Started/exercises/2.1/python/Insertion%20Sort%20Descending.py)


---
***3. Write pseudocode for linear search, which scans through the sequence, looking for val. Using a loop invariant,
prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.***

_**Pseudo Code**_

```
linear_search(A, key)
    for i = 1 to A.length    
        // compare each item with the key
        if A[i] == key
            // if there is a match then return the index of item in array
            return i
    // no match found return None
    return Nil
```

[Java](https://github.com/pctablet505/CLRS/blob/master/Foundations/2%20-%20Getting%20Started/exercises/2.1/java/LinearSearch.java)

[Python](https://github.com/pctablet505/CLRS/blob/master/Foundations/2%20-%20Getting%20Started/exercises/2.1/python/Linear%20Search.py)

### _Proof_

#### Invariant : If we are at i-th element of array, any one of two cases can happen :
 - a[i] is equal _val_, then simply we found the element no need to check more.
 - _val_ doesn't exists in a[0..i]


**_Initialization: It is true prior to start of the loop_**
- since, we haven't encountered any elements so far, it is true.

***Maintenance: If it is true before an iteration of the loop, it remains true before the next iteration.***
- Let's assume invariant is true upto _i-th index_.
- Case 1 -> **(a[i+1] is equal to _val_)**
  - then, simply we found the element and we don't need to check more.
- Case 2 -> **(a[i+1] is not equal to _val_)**
  - then, we know it is true upto i-th index and a[i+1] != _val_ , thus we conclude that, the invariant is maintained.

***Termination: When the loop terminates, the invariant gives us a useful property that helps show that the algorithm is correct***
- after the termination of loop ,we can conclude that no element from
a[0..(a.length-1)] is equal to _val_. hence _val_ doesn't exists in array and simple print some special value. Thus invariant is also maintained here.

---
***4. Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. The sum of the
two integers should be stored in binary form in an (n + 1)-element array C. State the problem formally and write
pseudocode for adding the two integers.***

#TODO correction in Pseudocode as it is confusing.
**Pseudo Code**

```
def add(a, b):
    n = len(a)
    // Initialize a (n+1) bit array
    res = [0] * (n + 1)
    
    // Set carry bit to 0
    carry = 0
    for i = n downto 1
        // set the (i+1)th bit to xor of (i th bits of both numbers) and the carry bit
        res[i + 1] = a[i] ^ b[i] ^ carry
        
        // carry bit is the and of ith bits from both numbers
        carry = a[i] & b[i]  # and of bits
    
    set the (n+1)th bit from right to to carry bit. 
    res[0] = carry
    return res
```

[Java](https://github.com/pctablet505/CLRS/blob/master/Foundations/2%20-%20Getting%20Started/exercises/2.1/java/AddNumbers.java)

[Python](https://github.com/pctablet505/CLRS/blob/master/Foundations/2%20-%20Getting%20Started/exercises/2.1/python/Binary%20Addition%20for%202%20n%20bit%20integers.py)

---
