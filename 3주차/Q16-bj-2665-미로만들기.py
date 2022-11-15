# https://www.acmicpc.net/problem/2665



import sys

N = int(sys.stdin.readline())  # 한줄에 들어가는 방 수 (방의 갯수는 N^2)
maze = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

def bfs(s, maze):
    level = {s: 0}      # 단계(level)은 몇 스텝만에 시작노드에서 해당 노드로 갈 수 있는지를 의미
    weight = {s: 0}     # 각 노드까지 도달하는데 드는 최소 비용 
    i = 1               # 단계를 나타낼 i (다음 단계를 탐색할 때마다 +1)
    frontier = [s]      # frontier는 각 레벨에서 탐색하게 될 노드(단계마다 바뀜)
    while frontier:     # 탐색할 노드가 존재하지 않을 때까지
        nexts = []      # 다음 단계에서 탐색할 노드를 담을 리스트 
        for u in frontier:          # frontier에 있는 시작노드들에 대해
            edges = [(u[0]+1,u[1]), (u[0]-1,u[1]), (u[0],u[1]+1), (u[0],u[1]-1)]
            for v in edges:  #v: (0, 1)     
                if (0 <= v[0] <= N-1) and (0 <= v[1] <= N-1):  # 목적지 노드의 조건
                    if maze[v[0]][v[1]] == 0:
                        v_weight = 1
                    else:
                        v_weight = 0
                    if (v not in level):  
                        level[v] = i    # v의 레벨은 i단계
                        weight[v] = weight[u] + v_weight
                        nexts.append(v) # 탐색할 다음 노드에 v를 추가 
                    if (v in level) and (weight[v] > weight[u] + v_weight):
                        weight[v] = weight[u] + v_weight
                        nexts.append(v) # 탐색할 다음 노드에 v를 추가 
        frontier = nexts    # 추가 된 다음 노드들을 frontier에 올림
        i += 1
    print(weight[(N-1,N-1)])

bfs((0,0), maze)  
