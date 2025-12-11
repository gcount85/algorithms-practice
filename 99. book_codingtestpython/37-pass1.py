# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 크루스칼 알고리즘
# 35분 solved


def find(parents, x):  # x의 루트 노드를 찾음
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


# x, y의 루트가 다르면 랭크가 짧은 애를 긴 쪽으로 합침
def union(rank, parents, x, y):
    rx = find(parents, x)
    ry = find(parents, y)

    if rx == ry:
        return False

    if rank[rx] > rank[ry]:
        parents[ry] = rx
    elif rank[rx] < rank[ry]:
        parents[rx] = ry
    else:
        parents[ry] = rx
        rank[rx] += 1
    return True


def solution(n, costs):
    """
    1. costs를 비용 기준으로 오름차순 정렬
    2. find, union 정의 && parents 배열 초기화
    3. 정렬한 costs를 순회:
        2-1. source와 dest가 서로 다른 집합이면(다른 컴포넌트): 같은 집합으로 바꾸고 비용에 추가
            아니면: pass
    """

    costs.sort(key=lambda x: (x[2], x[0], x[1]))
    parents = list(range(n))
    rank = [0 for _ in range(n)]

    min_cost = 0
    for source, dest, cost in costs:
        if union(rank, parents, source, dest):
            min_cost += cost

    return min_cost
