# https://school.programmers.co.kr/learn/courses/30/lessons/42861
"""
크루스칼 알고리즘

"""


def find(parents, a):
    if parents[a] != a:
        parents[a] = find(parents, parents[a])
    return parents[a]


def union(parents, a, b):
    root_a, root_b = find(parents, a), find(parents, b)
    if root_a == root_b:
        return False
    parents[root_a] = root_b
    return True


def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parents = list(range(n))
    connected = 0
    answer = 0
    for e in costs:
        if connected == n - 1:
            break
        s, d, w = e
        if union(parents, s, d):
            answer += w
            connected += 1
    return answer
