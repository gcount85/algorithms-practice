# https://school.programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answer = []
    for start, end, k in commands:
        new_array = array[start - 1 : end]
        new_array.sort()
        answer.append(new_array[k - 1])
    return answer
