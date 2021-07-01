A, B = map(int, input().split())

def gcd(A,B):
    if B>A:
        (A, B) = (B, A)
    while B > 0:
        (A,B) = (B, A%B)
    
    return(int(A))  # 여긴 int 없어도 됨.

def lcm(A,B):
    return(int(A*B/gcd(A,B)))

print (gcd(A,B))
print (lcm(A,B))

# https://velog.io/@jwisgenius/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98

#https://m.blog.naver.com/okkam76/221306562506   이런것도