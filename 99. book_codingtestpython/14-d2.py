"""
https://school.programmers.co.kr/learn/courses/30/lessons/81303
"""


def solution(n, k, cmd):
    """
    1. 삭제된 애들 담을 stack, 각 행 기준 위 아래 행 번호를 기록할 up, down 리스트 (e.g. up[0]은 0행의 윗줄 인덱스, down[n-1]은 n-1행(마지막행)의 아랫줄 인덱스)
    2. k는 현재 행 위치
    3. [분기] 명령어를 해석한다.
        2-1. D X :
            - X 번 down 리스트를 따라간다
        2-2. U X :
            - X 번 up 리스트를 따라간다
        2-3 C :
            - 현재 행의 윗 행 번호 = up[k]
            - 현재 행의 아랫 행 번호 = down[k]
            - "현재 행의 윗 행 번호"의 "아랫 행 번호"를 "현재 행의 아랫 행 번호"로 바꾼다
                => 이때 현재 행이 0번이면 index range error 발생
                   그래서 배열 초기화 할 때 앞 뒤로 2칸 더 확보, k += 1로 초기화
            - "현재 행의 아랫 행 번호"의 "윗 행 번호"를 "현재 행의 윗 행 번호"로 바꾼다
        2-4 Z :
            - 되살린 인덱스 r = stack.pop()
            - 복구 된 행의 윗 행 번호 = up[r]
            - 복구 된 행의 아랫 행 번호 = down[r]
            - "복구 된 행의 윗 행 번호"의 "아랫 행 번호"를 r로 바꾼다.
            - "복구 된 행의 아랫 행 번호"의 "윗 행 번호"를 r로 바꾼다.
    4. 정답 배열 초기화
    5. 스택을 순회하면서
        삭제된 애들 index만 정답 배열 원소에 X 로 표기
    6. 정답 배열 문자열 join

    """
    stack = []
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 2)]
    k += 1
    for c in cmd:
        if c == "C":
            stack.append(k)
            down[up[k]] = down[k]
            up[down[k]] = up[k]
            if down[k] > n:  # ⚠️ 마지막 행 예외 처리
                k = up[k]
            else:
                k = down[k]
            continue
        elif c == "Z":
            r = stack.pop()
            down[up[r]] = r
            up[down[r]] = r
            continue

        command, X = c.split(" ")
        X = int(X)
        if command == "D":
            for _ in range(X):
                k = down[k]
        else:
            for _ in range(X):
                k = up[k]

    answer = ["O" for _ in range(n)]
    for e in stack:
        answer[e - 1] = "X"
    return "".join(answer)
