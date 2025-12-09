# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3


def solution(n, computers):
    """
    1. answer 초기화
    2. visited 초기화
    3. start 노드부터 dfs, 한 번의 dfs 탐색이 끝날 때마다 answer ++1
    """

    answer = 0
    visited = set()

    for node in range(n):
        if node in visited:
            continue
        answer += 1

        stack = [node]
        while stack:
            cur = stack.pop()
            visited.add(cur)
            for i, v in enumerate(computers[cur]):
                if i not in visited and v == 1:
                    stack.append(i)

    return answer
