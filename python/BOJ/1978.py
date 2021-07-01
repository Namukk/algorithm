N = int(input())
answer = 0

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, x):	
        if x % i == 0:
    	    return False
    return True

a = list(map(int, input().split()))

for i in range(N):
    if is_prime_number(a[i]) == True:
        answer += 1

print(answer)


# https://velog.io/@koyo/python-is-prime-number     소수 판별식