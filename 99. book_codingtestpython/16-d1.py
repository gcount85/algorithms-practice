"""
- 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses
- 각 작업의 개발 속도가 적힌 정수 배열 speeds
- 각 배포마다 몇 개의 기능이 배포되는지를 return
"""


def solution(progresses, speeds):
    """
    93 + 1n = 100
    n = 100 - 93

    30 + 30n = 100
    n = (100-30)/30 = 2.X 실링 = 3

    1. progresses, speeds 두 배열을 순회
        1-1. 몇일차에 기능 완료되는지 전부 계산하여 deque에 저장
    2. 기능 완료 큐 다 pop할 때까지 반복
        2-1. popleft 해서 count ++1
        2-1. 다음 첫번째 원소가 popleft보다 작으면: count ++1
            아니면: 현재 count를 answer 배열에 추가 & count 0 초기화
    3. answer 배열 반환
    """
    from collections import deque
    import math

    days = deque()
    for p, s in zip(progresses, speeds):
        d = math.ceil((100 - p) / s)
        days.append(d)

    print("days:", days)
    answer = []
    while len(days) > 1:
        popped = days.popleft()  # 7
        count = 1
        while popped >= days[0]:
            popped = days.popleft()
            count += 1
            continue
        answer.append(count)
        days.appendleft(popped)
        count = 0
        print("days:", days)

    return answer
