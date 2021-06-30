import sys

while True:
    N = sys.stdin.readline().rstrip("\n")

    if not N:
        break
    a,b,c,d = 0,0,0,0
    for i in N:
        if i.islower():
            a += 1
        elif i.isupper():
            b += 1
        elif i.isdigit():
            c += 1
        elif i.isspace():
            d += 1
        
    print(a,b,c,d)
    # sys.stdout.write("{} {} {} {}\n".format(a, b, c, d))    이렇게 써도 됨




# https://velog.io/@jsj3282/%EB%B0%B1%EC%A4%80-10820%EB%B2%88-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B6%84%EC%84%9D-%ED%8C%8C%EC%9D%B4%EC%8D%AC    정답 참고

# https://somjang.tistory.com/entry/BaekJoon-10820%EB%B2%88-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B6%84%EC%84%9D-Python    이런 방법도


