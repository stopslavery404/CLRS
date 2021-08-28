# Utility function not part of algorithm
def preprocess(a, b):
    m = max(len(a), len(b))
    a = [0] * (m - len(a)) + a
    b = [0] * (m - len(b)) + b
    return a, b


def add(a, b):
    a, b = preprocess(a, b)  # So that both have same number of bits
    n = len(a)
    res = [0] * (n + 1)
    carry = 0
    for i in range(n - 1, -1, -1):
        res[i + 1] = a[i] ^ b[i] ^ carry  # xor of bits and carry bit
        carry = a[i] & b[i]  # and of bits

    res[0] = carry
    return res


a = [1, 1, 0, 0]
b = [1, 1, 1, 1]

print(add(a, b))
