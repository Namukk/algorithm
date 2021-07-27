import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([_+1 for _ in range(N)])


while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q.pop())


# https://yunaaaas.tistory.com/31   답 참고
# https://tooo1.tistory.com/88   이런 방식도(시간복잡도 참고)
# https://suri78.tistory.com/50   처음 내 생각이랑 비슷 