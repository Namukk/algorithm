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


# https://pacific-ocean.tistory.com/349
# https://velog.io/@sch804/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1012%EB%B2%88-%EC%9C%A0%EA%B8%B0%EB%86%8D-%EB%B0%B0%EC%B6%94