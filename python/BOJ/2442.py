N = int(input())

for i in range(1, N+1):
    print(" "*(N-i)+ "*"*((2*i)-1))

# 오답
# N = int(input())

# for i in range(1, N+1):
#     print(" "*(N-i)+ "*"*((2*i)-1) + " "*(N-i))