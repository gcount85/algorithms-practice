"""
https://school.programmers.co.kr/learn/courses/30/lessons/12949
행렬 곱셈은 첫번째 행렬의 행, 두번째 행렬의 열 기준으로 각각 원소끼리 곱한뒤 다 더함
100x100 * 100x100 이라고 하면.. 최대 연산 회수는 100^3 = 1000000 번 =>
"""


def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    # answer = [[0] * col] * row # ⚠️ 이렇게 쓰면 안 됨! mutable 객체를 * 연산자로 반복하면 참조를 함
    answer = [[0] * col for _ in range(row)]
    # print(answer)
    for r in range(row):  # 0, 1, 2
        for c in range(col):
            for i, v in enumerate(arr1[r]):  # [1, 4]
                # v는 3, 2, i는 0~1
                # 정답 행렬의 r행 c열의 값은 A[r] 행과 B의 c열을 곱한 것
                answer[r][c] += v * arr2[i][c]
                # print(v, arr2[i][c])
            # print(r, c, answer[r][c])

    return answer
