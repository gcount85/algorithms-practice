def preorder(arr, i, answer):
    """
    전위 순회
    1. 본인 방문
    2. 왼쪽 자식 노드 방문
    3. 오른쪽 자식 노드 방문
    """
    if i < len(arr):
        answer.append(arr[i])
        preorder(arr, i * 2 + 1, answer)
        preorder(arr, i * 2 + 2, answer)
        return answer


def inorder(arr, i, answer):
    """
    중위 순회
    1. 왼쪽 자식 노드 방문
    2. 본인 방문
    3. 오른쪽 자식 노드 방문
    """
    if i < len(arr):
        inorder(arr, i * 2 + 1, answer)
        answer.append(arr[i])
        inorder(arr, i * 2 + 2, answer)
        return answer


def postorder(arr, i, answer):
    """
    후위 순회
    1. 왼쪽 자식 노드 방문
    2. 오른쪽 자식 노드 방문
    3. 본인 방문
    """
    if i < len(arr):
        postorder(arr, i * 2 + 1, answer)
        postorder(arr, i * 2 + 2, answer)
        answer.append(arr[i])
        return answer


def solution(arr):
    a1 = preorder(arr, 0, [])
    b1 = inorder(arr, 0, [])
    c1 = postorder(arr, 0, [])
    return [
        " ".join(map(str, a1)),
        " ".join(map(str, b1)),
        " ".join(map(str, c1)),
    ]


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(
    solution([1, 2, 3, 4, 5, 6, 7])
)  # 반환값 : ["1 2 4 5 3 6 7", "4 2 5 1 6 3 7", "4 5 2 6 7 3 1"]
