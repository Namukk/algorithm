import sys
N = int(sys.stdin.readline())
stack = []

for i in range(N):
    a = sys.stdin.readline().split()

    if a[0] == "push":
        stack.append(a[1])
    elif a[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif a[0] == "size":
        print(len(stack))
    elif a[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


# https://velog.io/@wjdtmdgml/%EB%B0%B1%EC%A4%80%EC%8A%A4%ED%83%9D10828%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EC%8A%A4%ED%83%9D     참고