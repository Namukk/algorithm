T = 1000001
L = [True] * 1000001

for i in range(2, int((T-1)**0.5)+1):
    if L[i]:
        for j in range(i+i, T, i):
            L[j] = False

while True:
    N = int(input())
    flag = 0

    if N == 0:
        break

    for a in range(3, T):
        if L[a] and L[N-a]:
            print(str(N) + " = " + str(a) + " + " + str(N-a))
            flag = 1
            break

    if flag == 0:
        print("Goldbach's conjecture is wrong.")


# https://yuuj.tistory.com/157   답 참고
# https://yoonsang-it.tistory.com/52  이런 방법도

# 이건 소수 판별식
# def is_prime_number(x):
#     if x == 1:
#         return False
#     for i in range(2, int(x**0.5)+1):	  
#         if x % i == 0:
#     	    return False
#     return True