N = int(input())
L=[]

for i in range(N):
    a,b = map(str, input().split())
    a = int(a)
    L.append([a,b])

sorted_L = sorted(L, key=lambda x : x[0])

for j in range(N):
    print(sorted_L[j][0], sorted_L[j][1])

# for j in sorted_L:
#     print(j[0], j[1])



