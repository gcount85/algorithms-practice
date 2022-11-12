import sys

V, E = map(int, sys.stdin.readline().split())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]

'''
노드는 1번부터 V번까지 존재 
'''

# V = 3  # 노드개수 
# E = 3  # 엣지갯수
# W = [[1, 2, 1],
#      [2, 3, 2],
#      [1, 3, 3]]

# 가중치의 합 
uncovered = list(range(2,V+1))
total = 0

while len(uncovered) != 0:
    tmp = 2147483648
    for v in W:
        if ((v[0] not in uncovered) and (v[1] in uncovered)) or ((v[1] not in uncovered) and (v[0] in uncovered)):
            if (tmp >= v[2]):
                tmp = v[2]
                mini_edge = v  # 최소가중치를 가진 엣지
    total += mini_edge[2]
    src = mini_edge[0]
    dst = mini_edge[1]
    for j in W:
        if (j[0] == src and j[1] == dst) or (j[0] == dst and j[1] == src):
            W.remove(j)
    uncovered.remove(dst)

# 최소 스패닝 트리의 가중치를 출력
print(total)


'''슈도코드
bridges = 커버한 노드에서 안 커버한 노드로 가는 엣지들
모든 노드를 다 커버할 때까지 반복
    브릿지 중 최소 가중치를 가진 엣지 e를 찾음 
    e의 목적지를 커버한 노드에 추가
    e를 선택한 엣지 집합에 추가 
return 선택된 엣지 집합 E, 커버한 노드 U

엣지 집합 E에 대해서
    가중치를 모두 더함
return 가중치의 합 
'''







