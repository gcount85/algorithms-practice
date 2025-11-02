"""
https://school.programmers.co.kr/learn/courses/30/lessons/64061?language=python3
- "N x N" 크기의 정사각 격자
    - 가장 아래칸부터 쌓임
    - n은 5 ~ 30까지
    - 0은 빈칸, 1~100은 인형
- 크레인은 좌우로 움직임 (x축 이동)
    - moves 원소: 1~N
- 바구니
    - 바구니에 담을 때 연속 두개 -> 폭발
    - 바구니는 크기 제한 X
    - 폭발 할 때마다 카운팅 * 2

[[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1]],

50분만에 품
"""


def solution(board, moves):
    """
    1. [반복] moves 배열을 순회
        1-1. boards 의 위치에 가서 주인공 원소를 추출한다.
            // 예외 처리: 0이면 continue
        1-2. 스택이 있고, top이 주인공 원소랑 같다면 반복:
            pop, count++1
            또 pop 한 원소를 주인공 원소로 할당
        1-3. 주인공 원소를 스택에 담는다.
    2. 카운트 반환
    """
    stack = []
    count = 0
    for e in moves:
        col_index = e - 1
        push_candid = 0
        for row in board:
            if row[col_index] != 0:
                push_candid = row[col_index]
                row[col_index] = 0
                break
        if push_candid == 0:
            continue
        while stack and stack[-1] == push_candid:
            stack.pop()  # []
            count += 2
            if not stack:
                break
            push_candid = stack.pop()
        else:
            stack.append(push_candid)
    return count
