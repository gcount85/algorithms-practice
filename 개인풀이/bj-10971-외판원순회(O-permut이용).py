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

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())  # 2 <= N <= 10
W = [list(map(int, input().split())) for _ in range(N)]
permut = list(permutations(range(N)))   # 도시 방문 순서를 나타낸 순열
min_cost = 1000000 * 10


def dfs(N):
    global min_cost
    for p in permut:
        temp_total = 0
        for i in range(N):  # 시작도시와 도착도시의 인덱스 설정
            if (i == N-1):  # 처음 출발 도시로 돌아와야 하는 경우
                j = 0
            else:
                j = i+1
            temp_cost = W[p[i]][p[j]]
            temp_total += temp_cost
            if (temp_cost == 0) or (temp_total >= min_cost):
                j = N  # 갈수 없는 경우의 cost를 비교하지 않게 하기 위한 조건 설정
                break
        if (j == 0) and (temp_total < min_cost): # 처음 출발 도시로 돌아왔고, cost 비교
            min_cost = temp_total


dfs(N)
print(min_cost)

# 0. 순열 뽑아냄
# 1. dfs 방문
# 2. 다음과 같은 조건을 만나면 되돌아감
#     1) i에서 j로 갈 수 없는 경우 (비용이 0인 경우)
#     2) 돌아오는 경우가 아닌데 똑같은 도시 재방문 (돌아오는 경우 판별하도록 하기) -> 순열로 처리
# 3. 이전 방문 비용을 변수에 저장 & 비교하여 min 값을 구하기 → 출력
