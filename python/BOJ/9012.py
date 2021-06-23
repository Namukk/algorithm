N = int(input())

for i in range(N):
    a = input()
    L = list(a)
    sum = 0

    for j in L:
        if j == "(":
            sum += 1
        elif j == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
    
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")



# https://wook-2124.tistory.com/442  내 답 참고

# https://velog.io/@cosmos/BOJ-9012-python 확인
# T = int(input())

# for i in range(T):
#     ps = list(input())
    
#     while len(ps) != 0:
#         if ps[0] == ')':
#             print('NO')
#             break
#         else:
#             if ')' in ps:
#                 ps.remove(')')
#                 ps.remove('(')
#             else:
#                 print("NO")
#                 break
#     if len(ps)==0:
#         print("YES")