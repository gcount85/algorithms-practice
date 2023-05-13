import sys

def bfs_visit(s, edges):
    # s 노드에서 bfs 탐색 시작
    level = {s: 0}
    queue = edges[s]
    i = 1
    while queue:
        frontier = []
        for node in queue:
            if node in level:
                continue
            level[node] = i
            frontier.extend(edges[node])
        i += 1
        queue = frontier
    return sum(level.values())

def bfs():
    # 시작 노드를 바꿔가며 탐색
    min_value = float('inf') 
    for s in range(1, n+1):
        if (temp := bfs_visit(s, edges)) < min_value:
            min_value = temp
            answer = s
    return answer

input = sys.stdin.readline
n, m = map(int, input().split())

edges = [[] for _ in range(n+1)]
for _ in range(m):
    s, d = map(int, input().split())
    edges[s].append(d)
    edges[d].append(s)

print(bfs()) # 시작노드와 최단 거리


"""
모두 탐색하는데 걸리는 최단 거리의 합


"""