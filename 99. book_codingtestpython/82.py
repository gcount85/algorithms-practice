# https://school.programmers.co.kr/learn/courses/30/lessons/12982
# 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.


def solution(d, budget):
    d.sort()
    answer = 0
    for money in d:
        diff = budget - money
        if diff < 0:
            break
        budget = diff
        answer += 1
    return answer
