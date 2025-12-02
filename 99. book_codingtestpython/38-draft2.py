"""
DFS - 스택

"""


def solution(graph, start):
    """
    1. 그래프를 우선 인접 행렬/인접 리스트로 만든다.
    2. visited 초기화, 스택 초기화
    3. 스택에 start 노드를 담는다.
    4. 스택에 내용물 없을 때까지 반복:
        4-1. 스택 원소 pop하고 노드 방문 체크
        4-2. start의 인접 노드 순회:
            4-2-1. visited 체크 안 되어 있으면 스택에 담음
    """

    ad_list = {}
    for e in graph:
        s, d = e
        if s not in ad_list:
            ad_list[s] = [d]
        else:
            ad_list[s].append(d)

    # print(ad_list)

    stack = [start]
    visited = {start}
    answer = []
    while stack:
        current = stack.pop()
        answer.append(current)
        print(answer)
        visited.add(current)
        if current in ad_list:
            for n in ad_list[current][
                ::-1
            ]:  # 역순으로 순회하면 노드를 오름차순으로 방문함
                if n not in visited:
                    stack.append(n)
    return answer


# print(
#     solution([["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"]], "A")
# )  # ['A', 'B'', 'C', 'D', ‘E’]

print(
    solution(
        [["A", "B"], ["A", "C"], ["B", "D"], ["B", "E"], ["C", "F"], ["E", "F"]], "A"
    )
)  # [‘A’, ‘B’, ‘D’, ‘E’, ‘F’, ‘C’]
