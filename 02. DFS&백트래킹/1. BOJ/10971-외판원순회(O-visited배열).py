# https://www.acmicpc.net/problem/10971

"""
1번부터 N번까지 번호가 매겨져 있는 도시들이 있고,
도시들 사이에는 길이 있다. (길이 없을 수도 있다)
한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 경로를 구하려고 함
단, 한 번 갔던 도시로는 다시 갈 수 없다. (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외)
가장 적은 비용을 들이는 여행 계획은?

W[i][j]는 도시 i에서 도시 j로 가기 위한 비용
W[i][j] 는 W[j][i]와 다를 수 있다.
모든 도시간의 비용은 양의 정수이다.
W[i][i]는 항상 0이다.
W[i][j]=0는 도시 i에서 도시 j로 갈 수 없는 경우

첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 10)
다음 N개의 줄에는 비용 행렬이 주어진다.
각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다.
"""

import sys
input = sys.stdin.readline

N = int(input())  # 2 <= N <= 10
W = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
min_cost = 1000000 * 10


def dfs_visit(start, cost, visited):   # 목적지 도시 -> 시작 도시
    global min_cost

    if (cost >= min_cost):
        return
    if (sum(visited) == N-1):
        if (W[start][0] != 0):
            min_cost = min(min_cost, cost + W[start][0])
        return

    for dest in range(1, N):
        if (W[start][dest] != 0) and (visited[dest] == 0):
            visited[dest] = 1
            dfs_visit(dest, cost + W[start][dest], visited)
            visited[dest] = 0


def dfs(N):
    for d in range(1, N):
        if (W[0][d] != 0) and (visited[d] == 0):
            visited[d] = 1
            dfs_visit(d, W[0][d], visited)
            visited[d] = 0


dfs(N)
print(min_cost)

# 0. visited 1차원 배열 할당
# 1. dfs 방문
#   1) visited 확인 후 방문하지 않은 경우만 방문 (가장 작은 값을 먼저 방문하게 하면? -> 정답 보장X)
#   2. 다음과 같은 조건을 만나면 되돌아감
#       1) i에서 j로 갈 수 없는 경우 (비용이 0인 경우)
#       2) 돌아오는 경우가 아닌데 똑같은 도시 재방문
#   3. 다시 원래 도시로 돌아온 경우
#       1) min_cost 값과 비교하여 min 값 결정 → 출력
