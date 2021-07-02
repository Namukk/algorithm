N = int(input())
L = 1

if N == 0:
    print(L)
elif N != 0:
    for i in range(1, N+1):
        L *= i
    print(L)

