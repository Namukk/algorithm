import sys

node = int(input())
node_graph = [[] for _ in range(node + 1)]
parent = [[] for _ in range(node + 1)]

#트리를 그래프 형태로 생성

for _ in range(node - 1):
    i, j = map(int, sys.stdin.readline().split())
    node_graph[i].append(j)
    node_graph[j].append(i)

#DFS나 BFS나 무관

def dfs(graph_list, start, parent):
    stack = [start]
    
    while stack:
        node = stack.pop()
        for i in graph_list[node]:
            parent[i].append(node)
            stack.append(i)
            graph_list[i].remove(node)
    return parent

for i in dfs(node_graph, 1, parent)[2:]:
    print(i[0])


# https://claude-u.tistory.com/192    답 참고
# https://yongku.tistory.com/1968     dfs 다른 식
# https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-11725%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Tree-dfs-bfs      bfs 식