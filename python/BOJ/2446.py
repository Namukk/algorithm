N = int(input())

for i in range(1, N+1):
    print(" "*(i-1) + "*"*((2*N)-(2*i-1)))

for j in range(1, N):
    print(" "*(N-1-j) + "*"*(2*j+1))