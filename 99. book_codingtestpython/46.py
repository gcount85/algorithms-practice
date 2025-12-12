# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 27분 solved

from collections import defaultdict


def solution(n, wires):
    """
    트리 형태 -> 싸이클이 없다.. 끊을 때마다 서로 다른 컴포넌트인지 확인할 필요 없다. 하나를 끊으면 무조건 둘로 나뉨.
    1. 송전탑 차이 변수 초기화
    2. i 반복:
        1-1. wires 순회:
            1-1-1. i번째 요소를 끊는다.
            1-1-2. 인접 리스트 만든다.
        1-2. 송전탑 개수 변수 초기화, 스택 초기화
        1-3. 인접리스트로 dfs 하면서 컴포넌트 바뀔 때마다 차이를 update

    """

    min_diff = float("inf")
    for i in range(n - 1):
        tree = defaultdict(list)
        for j, (source, dest) in enumerate(wires):
            if i == j:
                continue
            tree[source - 1].append(dest - 1)
            tree[dest - 1].append(source - 1)

        visited = set()
        stack = [0]
        count = 0
        while stack:
            cur = stack.pop()
            visited.add(cur)
            count += 1
            for nxt in tree[cur]:
                if nxt not in visited:
                    stack.append(nxt)
        min_diff = min(min_diff, abs(n - count - count))

    return min_diff
