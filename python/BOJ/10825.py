N = int(input())
L=[]

for i in range(N):
    a, b, c, d = map(str, input().split())
    b = int(b)
    c = int(c)
    d = int(d)
    L.append([a, b, c, d])

sorted_L = sorted(L, key=lambda x : (-x[1], x[2], -x[3], x[0]))

for j in range(N):
    print(sorted_L[j][0])
