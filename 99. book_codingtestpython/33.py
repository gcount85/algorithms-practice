def find(disjoint_set, x):
    """
    x가 속한 집합의 대표 원소 = 루트 노드를 찾는다.
    """
    if disjoint_set[x] == x:
        return x

    # x가 루트 노드가 아니면 루트를 재귀적으로 찾은 다음에 경로 압축 후 반환
    disjoint_set[x] = find(disjoint_set, disjoint_set[x])
    return disjoint_set[x]


def union(disjoint_set, x, y, rank_data):
    """
    x, y가 속한 두 집합을 합친다.
    - 루트 노드가 서로 다르다면 같게 만든다.
    - 합칠 때 랭크가 작은 쪽을 랭크 큰 쪽에 붙인다.
    """

    root_x = find(disjoint_set, x)
    root_y = find(disjoint_set, y)
    rank_x = rank_data[x]
    rank_y = rank_data[y]
    if root_x != root_y:
        if rank_x > rank_y:
            disjoint_set[root_y] = root_x
        else:
            disjoint_set[root_x] = root_y
    return disjoint_set


def solution(k, operations):
    disjoint_set = list(range(k))
    rank_data = [0] * k
    answer = []
    for o in operations:
        x, y = map(int, o[1:])
        if o[0] == "u":
            disjoint_set = union(disjoint_set, x, y, rank_data)
        else:
            answer.append(find(disjoint_set, x) == find(disjoint_set, y))
    return answer


print(solution(3, [["u", "0", "1"], ["u", "1", "2"], ["f", "0", "2"]]))  # [true]
print(
    solution(4, [["u", "0", "1"], ["u", "2", "3"], ["f", "0", "1"], ["f", "0", "2"]])
)  # [true, false]
