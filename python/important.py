#최대공약수, 최소공배수
def gcd(A,B):
    if B>A:
        (A, B) = (B, A)
    while B > 0:
        (A,B) = (B, A%B)
    
    return(int(A))  # 여긴 int 없어도 됨.

def lcm(A,B):
    return(int(A*B/gcd(A,B)))


# bfs dfs
from collections import deque

N, M, V = map(int, input().split())
s = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    start_node, end_node = map(int, input().split())
    s[start_node][end_node] = 1
    s[end_node][start_node] = 1 

def bfs(V):
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
bfs(V)


#시간 덜 드는 bfs
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


#제곱근까지 소수 판별기
def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):	    # 소수는 제곱근까지만 검사하면 됨.
        if x % i == 0:
    	    return False
    return True


#일반 소수 판별기
def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, x):	
        if x % i == 0:
    	    return False
    return True


#소수 이용한 골드바흐
T = 1000001
L = [True] * 1000001

for i in range(2, int((T-1)**0.5)+1):
    if L[i]:
        for j in range(i+i, T, i):
            L[j] = False

while True:
    N = int(input())
    flag = 0

    if N == 0:
        break

    for a in range(3, T):
        if L[a] and L[N-a]:
            print(str(N) + " = " + str(a) + " + " + str(N-a))
            flag = 1
            break

    if flag == 0:
        print("Goldbach's conjecture is wrong.")


#참고
import sys

while True:
    N = sys.stdin.readline().rstrip("\n")

    if not N:
        break
    a,b,c,d = 0,0,0,0
    for i in N:
        if i.islower():
            a += 1
        elif i.isupper():
            b += 1
        elif i.isdigit():
            c += 1
        elif i.isspace():
            d += 1
        
    print(a,b,c,d)
    # sys.stdout.write("{} {} {} {}\n".format(a, b, c, d))    이렇게 써도 됨