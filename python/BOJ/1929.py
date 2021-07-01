import sys
A, B = map(int, sys.stdin.readline().split())

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):	    # 소수는 제곱근까지만 검사하면 됨.
        if x % i == 0:
    	    return False
    return True

for i in range(A, B+1):
    if is_prime_number(i) == True:
        print(i)

# https://deokkk9.tistory.com/17 