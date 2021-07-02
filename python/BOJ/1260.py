from collections import deque

N, M, V = map(int, input().split())
s = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    start_node, end_node = map(int, input().split())
    s[start_node][end_node] = 1
    s[end_node][start_node] = 1 

def bfs(V, N):
    visit = [False for _ in range(N+1)]
    visit[V] = True
    q = deque()
    q.append(V)
    while q: 
        current_node = q.popleft()
        print(current_node, end=" ")
        for next_node, tmp in enumerate(s[current_node]):
            if tmp and not visit[next_node]:
                q.append(next_node)
                visit[next_node] = True

dfs_visit = [False for _ in range(N + 1)]     # 변수 업데이트 위해서
def dfs(V):
    dfs_visit[V] = True
    print(V, end=" ")
    for next_node, tmp in enumerate(s[V]):
        if tmp and not dfs_visit[next_node]:
            dfs(next_node)       

dfs(V)
print()
bfs(V, N)

# l = [10,45,12,5]
# for i in range(len(l)):
#     print(i, l[i])
# for idx, num in enumerate(l):
#     print(idx, num)