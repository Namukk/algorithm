import sys
N = int(sys.stdin.readline())
que = []

for i in range(N):
    a = sys.stdin.readline().split()

    if a[0] == "push":
        que.append(a[1])
    elif a[0] == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop(0))
    elif a[0] == "size":
        print(len(que))
    elif a[0] == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif a[0] == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])


#  https://jacoblog.tistory.com/2  참고

# https://hongku.tistory.com/263   참고 22