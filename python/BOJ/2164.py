import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([_+1 for _ in range(N)])


while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q.pop())