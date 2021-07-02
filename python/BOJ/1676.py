import sys
N = int(sys.stdin.readline())

A = 1
count = 0

for i in range (1, N+1):
       A *= i
a = list(map(int,str(A)))
a = list(reversed(a))

for i in a:
    if i == 0:
        count += 1
    elif i != 0:
        break

print(count)
