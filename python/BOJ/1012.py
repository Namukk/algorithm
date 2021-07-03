from collections import deque

T = int(input())
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x, y):
    q = deque()
    q.append([x,y])
    while q: 
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and S[nx][ny] == 1:
                S[nx][ny] = 0
                q.append([nx,ny])        


for _ in range(T):
    M,N,K = map(int, input().split())
    S = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    for _ in range(K):
        c, d = map(int, input().split())
        S[d][c] = 1
    for v in range(N):
        for w in range(M):
            if S[v][w] == 1:
                bfs(v, w)
                S[v][w] = 0
                count += 1
    print(count)
        