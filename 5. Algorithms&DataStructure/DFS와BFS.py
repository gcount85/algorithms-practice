# https://www.acmicpc.net/problem/1260 이 문제를 참고함
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000),
# 간선의 개수 M(1 ≤ M ≤ 10,000),
# 탐색을 시작할 정점의 번호 V

from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    src, dst = map(int, sys.stdin.readline().split())
    edges[src].append(dst)
    edges[dst].append(src)  # 양방향이기에 이 라인이 없으면 오답

for i in edges:    # 숫자가 적은 노드부터 방문해야해서 오름차순 정렬함
    if i != []:
        i.sort()


def bfs(s, edges):
    level = {s: 0}      # 단계(level)은 몇 스텝만에 시작노드에서 해당 노드로 갈 수 있는지를 의미
    parent = {s: None}  # 특정 노드의 부모 노드(전 단계에 있던 노드)를 가리킴
    i = 1               # 단계를 나타낼 i (다음 단계를 탐색할 때마다 +1)
    frontier = [s]      # frontier는 각 레벨에서 탐색하게 될 노드(단계마다 바뀜)
    print(s, end=' ')
    while frontier:     # 탐색할 노드가 존재하지 않을 때까지
        nexts = []      # 다음 단계에서 탐색할 노드를 담을 리스트
        for u in frontier:          # frontier에 있는 시작노드 s에 대해
            for v in edges[u]:      # 그 시작노드가 가진 엣지들의 목적지 노드에 대해
                if v not in level:  # 목적지 노드가 level에 없다면
                    level[v] = i    # v의 레벨은 i단계
                    parent[v] = u   # v의 부모 노드는 u
                    print(v, end=' ')
                    nexts.append(v)  # 탐색할 다음 노드에 v를 추가
        frontier = nexts    # 추가 된 다음 노드들을 frontier에 올림
        i += 1


# 큐를 이용한 BFS 의사코드


def BFS(graph, start_node):
    visited = set()  # 방문한 노드를 저장할 집합
    queue = deque([start_node])  # 탐색할 노드를 저장할 큐

    while queue:
        current_node = queue.popleft()  # 큐에서 첫 번째 노드를 꺼낸다.

        if current_node not in visited:  # 현재 노드가 방문한 적이 없다면
            visited.add(current_node)  # 방문한 노드로 표시하고
            # 인접한 노드 중 방문하지 않은 노드를 큐에 추가한다.
            queue.extend(
                neighbor for neighbor in graph[current_node] if neighbor not in visited)

    return visited


# 사용 예시:
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2],
    6: [3],
    7: [3]
}

start_node = 1
visited_nodes = BFS(graph, start_node)
print(visited_nodes)


parent = {}          # 부모 노드를 지정해줌으로써 이미 방문했는지 아닌지 판별


def dfs_visit(s, edges):
    for v in edges[s]:      # 시작 노드의 목적지 노드들에 대해서
        if v not in parent:  # 목적지 노드의 부모노드가 지정되지 않았다면(이전에 방문 안 했으면)
            parent[v] = s   # 시작 노드를 해당 노드의 부모노드로 지정
            dfs_visit(v, edges)  # 해당 목적지 노드를 대상으로 재귀

# dfs 함수는 단절된 그래프, 강하게 연결된 그래프가 아닌 경우에 시작 노드를 바꿔 모든 그래프를 탐색하기 위함


def dfs(N, edges):
    for s in range(1, N+1):  # 모든 노드들에 대해
        if s not in parent:  # 이미 방문된 노드가 아니라면
            parent[s] = None   # '부모 없음'을 뜻하는 None으로 저장; dfs_visit을 시작할 노드이기 때문
            dfs_visit(s, edges)


bfs(V, edges)
dfs(V, edges)
