# 35분 경과

"""
- 가장 y가 큰 게 루트
- 그 다음 작은 y를 가진 노드가 루트의 자식 노드
- 본인보다 작은 x, 큰 x를 가지면서 본인의 부모보다 작은/큰 x를 갖는 게 나의 서브트리 => 이걸 반복

"""


def find_right_child(sorted_node, current):
    """
    1. current보다 작은 y를 가지면서
    2. current보다 큰 x를 가지는 애
    """


def preorder(pre, current):
    pre.append(current[1])
    preorder(pre)  # 왼쪽자식
    preorder(pre)  # 오른쪽 자식


def postorder(current):
    postorder()  # 왼쪽자식
    postorder()  # 오른쪽 자식
    post.append(current)


def solution(nodeinfo):
    dic = {}
    for i, v in enumerate(nodeinfo):
        dic[(v[0], v[1])] = i + 1

    # (y 내림, x 오름)으로 정렬
    sorted_node = sorted(dic.items(), key=lambda x: (-x[0][1], x[0][0]))
    print(sorted_node)

    root = sorted_node[0]

    pre = []
    preorder(pre, root)

    # post = []

    answer = [[]]
    return answer
