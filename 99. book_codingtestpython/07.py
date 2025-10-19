"""
https://school.programmers.co.kr/learn/courses/30/lessons/49994
게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이 => 처음 가본 간선 개수 (x, y) <-> (s, d)
"""


def solution(dirs):  # 명령어 string, 1~500개 => n^2 까지는 ㄱㅊ 을듯
    """
    (0,0) -> (1,0),(0,1),(-1,0),(0,-1)
    (0,0) -> (1,0) 으로 갔다가, (1,0) -> (0,0) 으로 간다면?
    (0,0) -> (0,1)

    - dirs 반복문을 돌린다
        - 한 칸 움직일 때마다, 이동 전 위치, 이동 후 위치를 알아낸다.
        - 무방향 간선으로 set에 저장한다
    - 마지막에 set 개수 반환

    """
    move = set()
    x = 0
    y = 0
    for d in dirs:
        dx, dy = x, y
        if d == "U":
            dy = y + 1
        if d == "D":
            dy = y - 1
        if d == "R":
            dx = x + 1
        if d == "L":
            dx = x - 1
        if dx > 5 or dy > 5 or dx < -5 or dy < -5:
            continue
        now = (x, y)
        dest = (dx, dy)
        if now < dest:
            move.add((now, dest))
        else:
            move.add((dest, now))
        x = dx
        y = dy
        # print(move)
    answer = len(move)
    return answer
