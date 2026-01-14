# https://school.programmers.co.kr/learn/courses/30/lessons/81302

"""
px p -> O
po p -> X
pp -> X
dfs
"""


def can_go(x, y, place):
    if x >= 5 or y >= 5 or x < 0 or y < 0:
        return False
    if place[x][y] == "X":
        return False
    return True


def solution(places):
    """
    1. 스택 초기화, 방문 딕셔너리 초기화
    2. (0, 0)부터 dfs 시작
    3. 이전 2스텝 저장: pop, pp 패턴이면 바로 1 반환하고 탐색 종료
       ㄴ 거리 값 들고 다니면서 2 이하에 P를 만나면 리턴
    """

    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    answer = []

    def dfs(place):
        nonlocal direction, answer

        for i in range(5):
            for j in range(5):
                if place[i][j] != "P":
                    continue

                stack = [(i, j, 0)]
                visited = {(i, j)}
                while stack:
                    curx, cury, distance = stack.pop()
                    if distance >= 2:
                        continue

                    # 사방 조사
                    for x, y in direction:
                        nx, ny = curx + x, cury + y
                        if not can_go(nx, ny, place):
                            continue
                        if (nx, ny) in visited:
                            continue
                        if place[nx][ny] == "P":
                            answer.append(0)
                            return
                        stack.append((nx, ny, distance + 1))
                        visited.add((nx, ny))
        answer.append(1)

    for p in places:
        dfs(p)

    return answer
