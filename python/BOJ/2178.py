N, M = map(int, input().split())
s = []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    s.append(list(input()))
queue = [[0, 0]]
s[0][0] = 1

while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < N and 0 <= y < M and s[x][y] == "1":
            queue.append([x, y])
            s[x][y] = s[a][b] + 1

print(s[N - 1][M - 1])


# https://pacific-ocean.tistory.com/265    답 참고