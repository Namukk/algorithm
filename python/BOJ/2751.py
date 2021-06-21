N=int(input())
L=[]

for i in range(N):
    a=int(input())
    L.append(a)

sorted_L = sorted(L)

for j in sorted_L:
    print(j)


# 다른 내 정답
# N = int(input())
# num = []

# for i in range(N):
#     num.append(int(input()))

# num = sorted(set(num))

# for i in num:
#     print(i)