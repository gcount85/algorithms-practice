import sys

V, E = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(E)]
for _ in range(E):
    src, dst, w = map(int, sys.stdin.readline().split()) 
    edges[src].append((dst, w))   

# print(edges)

'''
노드는 1번부터 V번까지 존재 
'''
# V = 3  # 노드개수 
# E = 3  # 엣지갯수
# W = [[1, 2, 1],
#      [2, 3, 2],
#      [1, 3, 3]]
# V = 3  # 노드개수 
# E = 4  # 엣지갯수
# W = [[1, 2, 1],
#      [2, 1, 1],
#      [2, 3, 3],
#      [3, 1, 0]]

# 가중치의 합 
covered = [1] + [[] for _ in range(V-1)]
# print(covered)
chk = set()
total = 0

while len(chk) != V:
    tmp = 2147483648
    for i, v in enumerate(edges):      # i = 0,1,2   #v = [], [(2, 1), (3, 3)], [(3, 2)]
        if (i > 0) and (covered[i-1] != [] and v != []):  # 해당 노드가 커버되어있고, 그 노드에서 다른 노드로 가는 엣지들이 존재할 때
            for j in v:  # [(2, 1), (3, 3)]
                if (covered[j[0]-1] == []) and (tmp > j[1]):
                    tmp = j[1]
                    mini_edge = j  # 최소가중치를 가진 엣지의 (dst, 가중치)
                    src = i
    total += mini_edge[1]
    covered[src-1] = src    
    dst = mini_edge[0]
    covered[dst-1] = dst 
    chk.add(src)
    chk.add(dst)
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







