# https://school.programmers.co.kr/learn/courses/30/lessons/92345

"""
dfs(state) → (can_win, moves)
can_win = True  : 현재 턴 플레이어가 최적 플레이하면 이김
can_win = False : 현재 턴 플레이어가 아무리 잘 해도 짐
moves = 그 결과가 확정될 때까지의 총 이동 횟수

dfs(board, a_pos, b_pos, turn):
    # turn: 지금 움직일 플레이어 (A or B)

    1. 종료 조건
        - 현재 턴 플레이어가 서 있는 발판이 0이거나
        - 현재 턴 플레이어가 이동할 수 있는 곳이 하나도 없으면
            → return (False, 0)
            # 현재 턴 플레이어 패배

    2. 가능한 모든 이동에 대해 결과 수집
        results = []

        for each possible move:
            - 현재 위치 발판 제거
            - 다음 상태로 dfs 호출
              (상대 턴, 이동 후 위치)
            - 결과 (opp_can_win, opp_moves) 받음
            - results에 (opp_can_win, opp_moves + 1) 저장
            - 발판 복구

    3. 결과 판정 (미니맥스 핵심)
        3-1. 상대가 지는 경우가 하나라도 있다면
             (opp_can_win == False)
            → 나는 이길 수 있음
            → 가장 빨리 이기는 경우 선택
            → return (True, min(moves of losing cases))

        3-2. 모든 경우에서 상대가 이긴다면
            → 나는 무조건 짐
            → 최대한 오래 버티는 경우 선택
            → return (False, max(moves of all cases))

"""

"""
- dfs returns 지금 현재 내 입장에서 can_win(bool), steps
- dfs
1. A가 갈 수 있는 사방 위치에 대해서:
    1-0. 만약 a == b 위치가 같음 > return True, step + 1
    1-1. dfs 수행
    1-2. dfs 결과를 저장(steps)
    1-3. 만약 항상 지는 결과가 나왓다: return False, max(lose_step)
    1-4. 이길 수도 있다: return True, min(win_step)
2. 갈 수 있는 곳이 없음: return False, step
"""


def can_go(board, x, y, row, col):
    if x < 0 or y < 0 or x >= row or y >= col or board[x][y] == 0:
        return False
    return True


def solution(board, aloc, bloc):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    row = len(board)
    col = len(board[0])

    def dfs(aloc, bloc, steps):  # return can_win, steps
        nonlocal direction, board

        # ✅ 추가: 현재 턴 플레이어가 서있는 발판이 0이면 즉시 패배
        if steps % 2 == 0 and board[aloc[0]][aloc[1]] == 0:
            return False, steps
        if steps % 2 == 1 and board[bloc[0]][bloc[1]] == 0:
            return False, steps

        # 항상 질 수밖에 없는지 여부, 이길때 걸음수, 질 때 걸음수
        always_lose, win_steps, lose_steps = True, [], []
        for x, y in direction:
            # A의 턴
            if steps % 2 == 0:
                nx, ny = aloc[0] + x, aloc[1] + y
                if not can_go(board, nx, ny, row, col):
                    continue
                if aloc == bloc:
                    return True, steps + 1
                board[aloc[0]][aloc[1]] = 0
                opp_win, total_steps = dfs((nx, ny), bloc, steps + 1)
                board[aloc[0]][aloc[1]] = 1

            # B의 턴
            else:
                nx, ny = bloc[0] + x, bloc[1] + y
                if not can_go(board, nx, ny, row, col):
                    continue
                if aloc == bloc:
                    return True, steps + 1
                board[bloc[0]][bloc[1]] = 0
                opp_win, total_steps = dfs(aloc, (nx, ny), steps + 1)
                board[bloc[0]][bloc[1]] = 1

            my_can_win = not opp_win

            if my_can_win:
                always_lose = False
            (win_steps if my_can_win else lose_steps).append(total_steps)

        if always_lose and lose_steps:
            return False, max(lose_steps)
        elif not always_lose and win_steps:
            return True, min(win_steps)
        return False, steps

    _, steps = dfs(aloc, bloc, 0)
    return steps
