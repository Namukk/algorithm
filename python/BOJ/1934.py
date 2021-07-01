N = int(input())

def gcd(A,B):
    if B > A:
        (A,B) = (B,A)
    while B > 0:
        (A,B) = (B, A%B)
    return int(A)

for i in range(N):
    A, B = map(int, input().split())
    print(int(A*B/gcd(A,B)))
    