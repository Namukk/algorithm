N = int(input())

for i in range(1, N+1):
    if i == N:
        print("*"*(2*i-1))
    elif i == 1:
        print(" "*(N-i) + "*")
    else:
        print(" "*(N-i) + "*" + " "*(2*i-3) + "*")
    


# https://cleancode-ws.tistory.com/52 참고
# https://jyeonnyang2.tistory.com/34?category=923069 ????? 확인
# https://jinyes-tistory.tistory.com/64 ????? 확인