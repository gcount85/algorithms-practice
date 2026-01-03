# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 최대 한 번에 2명


def solution(people, limit):
    people.sort()  # 오름차순 정렬

    n = len(people)
    start = 0
    end = n - 1
    answer = 0
    while start <= end:
        light = people[start]
        heavy = people[end]
        if light + heavy <= limit:
            start += 1
        answer += 1
        end -= 1

    return answer
