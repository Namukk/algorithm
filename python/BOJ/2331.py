A, P = map(int, input().split())
check = [0] * 236197  # 9 ** 5 + 9 ** 5 + 9 ** 5 + 9 ** 5 최대 인덱스의 값이기 때문
iteration = 1
# D = []
# D_ = 0

# 이렇게 물면 못품. => 중복된거를 뽑아낼 수가 없어
# D.append(str(A))
# for i in range(A):
#     for j in range(len(D[i])):
#         Z = (int(D[i][j])**P)
#         D_ += Z

#     D.append(str(D_))
#     D_ = 0

def Daum(A, P):
    n = str(A)
    res = 0
    for i in n:
        res += pow(int(i), P)
    return res

def dfs(A, P, iteration, check):
     # 이미 한 번 계산 됐다면, 이제 반복된다고 판단
    if check[A] != 0:
        #print(A)
        return check[A] - 1

    check[A] = iteration
    # print(A)
    daum = Daum(A, P)
    iteration += 1
    return dfs(daum, P, iteration, check)

print(dfs(A,P,iteration,check))


# https://goodsosbva.tistory.com/21   답 참고