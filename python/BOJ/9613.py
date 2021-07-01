N = int(input())

def gcd(A,B):
    if B > A:
        (A, B) = (B, A)
    while B > 0:
        (A, B) = (B, A % B)
    return A

for i in range(N):
    a = list(map(int, input().split()))
    b = a[0]
    answer = 0

    for j in range(1, b):
        for k in range(j+1, b+1):
            answer += gcd(a[j],a[k])
    # 제구's advice
    # for j in range(b):
    #     for k in range(b):
    #         if j < k:
    #             answer += gcd(a[j],a[k])
    
    print(answer)
        
        
    
        

