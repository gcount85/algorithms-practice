"""
https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=python3
서로 다른 인덱스에 있는 두 개의 수 뽑아서, 더해서 만들 수 있는 모든 수
중복은 안 됨
오름차순

"""


def solution(numbers):
    length = len(numbers)

    # 반복문 두개에 list 변환 -> N2 + N
    sum_list = list(
        {
            numbers[x] + numbers[y]
            for x in range(length)
            for y in range(length)
            if x != y
        }
    )

    # 정렬 -> NlogN
    sum_list.sort()

    return sum_list
