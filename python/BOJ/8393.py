N = int(input())
L=[]

for i in range(N+1):
    L.append(i)
    i=i+1

print(sum(L))


# 다른풀이
# a = int(input())
# sum = 0
# for i in range(a+1):
#     sum = sum + i
# print(sum)