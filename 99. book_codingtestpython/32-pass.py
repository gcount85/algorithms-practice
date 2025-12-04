# https://school.programmers.co.kr/learn/courses/30/lessons/42892?language=python3
# 1차 복습 40분 solved

import sys

sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, info):
        self.number = info[0]
        self.x = info[1]
        self.y = info[2]
        self.left_child = None
        self.right_child = None


def preorder(answer, node: Node):
    if not node:
        return
    answer.append(node.number)
    preorder(answer, node.left_child)
    preorder(answer, node.right_child)


def postorder(answer, node: Node):
    if not node:
        return
    postorder(answer, node.left_child)
    postorder(answer, node.right_child)
    answer.append(node.number)


def insert_node(root: Node, node):
    """
    1. 루트부터 왼쪽 노드를 붙임
        1-1. 더이상 노드가 없을 때까지 반복: 왼쪽 자식이 있는가?
    2. 2번을 오른쪽 노드에도 반복
    """
    x = node[1]
    parent = root
    while True:
        # 부모보다 x가 작아? => 왼쪽 자식으로 감
        if x < parent.x:
            if not parent.left_child:
                parent.left_child = Node(node)
                return
            parent = parent.left_child
        # 부모보다 x가 같거나 커? => 오른쪽 자식으로 감
        else:
            if not parent.right_child:
                parent.right_child = Node(node)
                return
            parent = parent.right_child


def solution(nodeinfo):
    """
    1. nodeinfo 순회하면서 노드 번호도 붙임
    2. nodeinfo 정렬, -y, +x
    3. insert_node
    4. 전위순회, 후위순회

    """
    sorted_node = []
    for i, v in enumerate(nodeinfo):
        sorted_node.append((i + 1, *v))

    sorted_node.sort(key=lambda x: (-x[2], x[1]))
    # print(sorted_node)

    # 루트 노드만 생성
    root = Node(sorted_node[0])

    # 노드를 트리에 삽입
    for i in range(1, len(sorted_node)):
        insert_node(root, sorted_node[i])

    preorder_answer = []
    postorder_answer = []

    preorder(preorder_answer, root)
    postorder(postorder_answer, root)

    answer = [preorder_answer, postorder_answer]
    return answer


print(
    solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
)  # [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
