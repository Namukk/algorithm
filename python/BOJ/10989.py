import sys
N = int(sys.stdin.readline())
L = []

for i in range(N):
    a = int(sys.stdin.readline())
    L.append(a)

sorted_L = sorted(L)

for j in range(N):
    print(sorted_L[j])