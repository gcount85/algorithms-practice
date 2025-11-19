class Node:
    def __init__(self, value, right_child, left_child):
        self.value = value
        self.right_child = right_child
        self.left_child = left_child


def search(target, current_node: Node):
    if not current_node:
        return False
    if target == current_node.value:
        return True
    if target > current_node.value:
        return search(target, current_node.right_child)
    else:
        return search(target, current_node.left_child)


def find_insert(target, current_node: Node):
    if target > current_node.value:
        if not current_node.right_child:
            current_node.right_child = Node(target, None, None)
        else:
            find_insert(target, current_node.right_child)
    else:
        if not current_node.left_child:
            current_node.left_child = Node(target, None, None)
        else:
            find_insert(target, current_node.left_child)


def create_bst(arr):
    """
    0. 루트면 start_node를 만들고 루트 값을 넣는다.
    1. arr의 루트 다음 원소부터 시작해서 순회?
        1-1. 탐색 자리를 찾는다(search랑 동일)
        1-2. 빈 공간을 찾으면 거기다가 연결한다.
    """

    start_node = Node(arr[0], None, None)
    for i in range(1, len(arr)):
        find_insert(arr[i], start_node)
    return start_node


def solution(arr, find):
    start_node = create_bst(arr)
    answer = []
    for e in find:
        a = search(e, start_node)
        answer.append(a)
    return answer


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6]))  # [True, True, True, False]
print(
    solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
)  # [False, False, False, False, False]
