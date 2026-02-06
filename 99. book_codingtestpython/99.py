# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    n, m = len(board), len(board[0])
    diff = [[0] * (m + 1) for _ in range(n + 1)]

    # 1) 차분 배열에 스킬 반영 (모서리 4개만)
    # 우리가 하고 싶은 것: 직사각형 영역 (r1,c1) ~ (r2,c2)에 전부 +d를 하고 싶다.
    for t, r1, c1, r2, c2, d in skill: # [type, r1, c1, r2, c2, degree]
        d = -d if t == 1 else d
        diff[r1][c1] += d
        diff[r1][c2 + 1] -= d
        diff[r2+1][c1] -= d
        diff[r2+1][c2+1] += d

    # 2) 가로 누적합
    for i in range(n):
        run = 0
        for j in range(m):
            run += diff[i][j]
            diff[i][j] = run

    # 3) 세로 누적합 + 생존 카운트
    answer = 0
    for j in range(m):
        run = 0
        for i in range(n):
            run += diff[i][j]
            if board[i][j] + run > 0:
                answer += 1

    return answer
