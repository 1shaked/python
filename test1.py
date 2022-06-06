
for n in range(25):
    total = 0
    for k in range(n):
        total += (((-1)**k) * -1) / (5**(n-k))
    print(total)


A = [x for x in range(25)]


print(A[4::])