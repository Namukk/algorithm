A, B = map(int, input().split())

def gcd(A, B):
    if B > A:
        (A, B) = (B, A)
    while B > 0:
        (A, B) = (B, A%B)
    return int(A)

print("1" * gcd(A, B))    # int 안해줘도 됨?   그냥 유클리드 쓰면 메모리 초과

# https://claude-u.tistory.com/404   참고