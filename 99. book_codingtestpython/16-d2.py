"""
https://school.programmers.co.kr/learn/courses/30/lessons/42586
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
        1-1. 몇일차에 기능 완료되는지 전부 계산하여 저장
    2. days 배열을 순회
        2-1. 최대 일수보다 같거나 작으면 ++count
            아니면 최대 일수 갈아끼고, count 초기화 & answer 배열 추가
    3. answer 배열 반환
    """
    import math

    days = []
    for p, s in zip(progresses, speeds):
        d = math.ceil((100 - p) / s)
        days.append(d)

    count = 0
    max_days = days[0]
    answer = []
    for e in days:
        if max_days >= e:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_days = max(max_days, e)
    answer.append(count)

    return answer
