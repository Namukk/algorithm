import sys
from collections import deque

# circle, line = int(input().split())
# L = [[0 for _ in range(circle+1)] for _ in range(circle+1)]

def bfs():
    q = deque()
    result = 0
    for i in range(1, u+1):
        if visit[i] == 0:
            visit[i] = 1
            q.append(i)
            result += 1
            while q: 
                current_node = q.popleft()
                for j in graph[current_node]:
                    if visit[j] == 0:
                        visit[j] = 1
                        q.append(j)
    print(result)

if __name__ == "__main__":
    u, v = map(int, sys.stdin.readline().split())
    graph = [[] * u for _ in range(u+1)]
    visit = [0] * (u+1)

    for i in range(v):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)
    bfs()


# https://myjamong.tistory.com/235   답 참고(bfs)

# https://pacific-ocean.tistory.com/268   dfs
# https://ywtechit.tistory.com/67