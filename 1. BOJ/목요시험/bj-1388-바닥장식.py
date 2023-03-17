# 만약 두 개의 ‘-’가 인접해 있고, 
# 같은 행에 있다면, 
# 두 개는 같은 나무 판자 
# 두 개의 ‘|’가 인접해 있고, 
# 같은 행에 있다면, 
# 두 개는 같은 나무 판자 

import sys

N, M = map(int, sys.stdin.readline().split())  # 세로크기 N, 가로크기M
floor = []
for i in range(N):
    board = list(sys.stdin.readline().rstrip())
    floor.append(board)
# print(floor)
# [['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-']]

count = 0
parent = {}

def dfs_visit(s: tuple, floor: list):
    pattern = floor[s[0]][s[1]]
    if floor[s[0]][s[1]] == '-':
        edge = [(s[0],s[1]+1), (s[0],s[1]-1)]
    else:
        edge = [(s[0]+1,s[1]), (s[0]-1,s[1])]
    for v in edge:
        if (0 <= v[0] <= N-1) and (0 <= v[1] <= M-1) and (v not in parent):  # 목적지 노드의 조건
            tmp = floor[v[0]][v[1]]
            if pattern == tmp: 
                parent[v] = s
                dfs_visit(v, floor)

# dfs 함수는 단절된 그래프, 강하게 연결된 그래프가 아닌 경우에 시작 노드를 바꿔 모든 그래프를 탐색하기 위함
def dfs(N, M, floor):  
    global count
    for i in range(N):  # 모든 노드들에 대해   #0,1,2,3
        for j in range(M):
            s = (i, j)
            if s not in parent: # 이미 방문된 노드가 아니라면
                parent[s] = None # '부모 없음'을 뜻하는 None; dfs_visit을 시작할 노드이기 때문
                count += 1
                dfs_visit(s, floor)

dfs(N, M, floor)
print(count)

