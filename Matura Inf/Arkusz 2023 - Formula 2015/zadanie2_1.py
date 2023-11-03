A = [1, 2, 3, 4]
n = 4

def f(p, q):
    if p != q:
        k = (q-p+1) // 2
        for i in range(0, k):
            # a, b = b, a
            A[p+i-1], A[q-k+i] = A[q-k+i], A[p+i-1]
        f(p, p+k-1)
        f(q-k+1, q)

f(1, n)
print(A)


# log^a b = c
# a^c = b
def log(a, b):
    for c in range(1, b):
        if a**c == b:
            return c
        c += 1