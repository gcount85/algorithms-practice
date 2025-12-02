"""
DFS - 재귀

"""


def dfs(answer, visited, ad_list, node):
    visited.add(node)
    answer.append(node)

    if node in ad_list:
        for n in ad_list[node]:
            if n not in visited:
                dfs(answer, visited, ad_list, n)


def solution(graph, start):
    """
    1. 그래프를 우선 인접 행렬/인접 리스트로 만든다.
    2. visited 초기화
    3. visited에 start 노드를 담는다.
    4. start의 인접 노드 순회:
        4-1. visited 체크 안 되어 있으면 dfs 재귀 호출
    """
    ad_list = {}
    for s, d in graph:
        if s not in ad_list:
            ad_list[s] = [d]
        else:
            ad_list[s].append(d)
    print(ad_list)

    visited = {start}
    answer = []
    dfs(answer, visited, ad_list, start)
    return answer


print(
    solution([["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"]], "A")
)  # ['A', 'B'', 'C', 'D', ‘E’]

print(
    solution(
        [["A", "B"], ["A", "C"], ["B", "D"], ["B", "E"], ["C", "F"], ["E", "F"]], "A"
    )
)  # [‘A’, ‘B’, ‘D’, ‘E’, ‘F’, ‘C’]
