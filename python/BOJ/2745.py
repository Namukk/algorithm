N, B = input().split()
B = int(B)
result = 0

for i, j in enumerate(N):
    try:
        if int(j):
            result += int(j) * B ** (len(N)-i-1)
    except:
        result += (ord(j)-55) * B ** (len(N)-i-1)
        
print(result)


# https://claude-u.tistory.com/462 
# https://somjang.tistory.com/entry/BaeKJoon-2745%EB%B2%88-%EC%A7%84%EB%B2%95-%EB%B3%80%ED%99%98-Python

# https://hooneee.tistory.com/86
# n, b = input().split()
# print(int(n, int(b)))