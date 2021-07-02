from collections import deque
import sys

M = int(sys.stdin.readline())  #컴퓨터 개수
N = int(sys.stdin.readline())  #연결된 선 수
V = 1


L=[[0 for _ in range(M+1)] for _ in range(M+1)]

for _ in range(N):
    start_node, end_node = map(int, sys.stdin.readline().split())
    L[start_node][end_node] = L[end_node][start_node] = 1

def bfs(V):
    visit = [V]
    # visit[V] = True    
    q = deque()
    count = 0
    q.append(V)
    while q:
        current_node = q.popleft()
        for next_node, tmp in enumerate(L[current_node]):
            if tmp and (next_node not in visit):
                q.append(next_node)
                visit.append(next_node)
                count += 1
    print(count)

bfs(1) 

# https://jokerldg.github.io/algorithm/2021/03/26/virus.html   참고