import sys
N = int(sys.stdin.readline())
deque = []

for i in range(N):
    a = sys.stdin.readline().split()
    
    if a[0] == "push_front":
        deque = [a[1]] + deque
    elif a[0] == "push_back":
        deque.append(a[1])
    elif a[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif a[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(-1))
    elif a[0] == "size":
        print(len(deque))
    elif a[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif a[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])


# https://jinu0418.tistory.com/63    참고