# https://school.programmers.co.kr/learn/courses/30/lessons/64065


def solution(s):
    """
    1. 일단 s 집합을 개수로 정렬을 함
    2. 정렬한 집합 s 길이만큼 반복:
        2-1. 원소가 1개면 걔가 1번
        2-2. 이전 집합을 현재 집합에서 빼고 남은 원소를 이어 붙임
    """
    t = s[2:-2].split("},{")  # O(N)
    t.sort(key=lambda x: len(x))  # O(MlogM)
    # print(t)
    answer = [int(t[0])]
    prev_set = set(t[0].split(","))
    for i in range(1, len(t)):
        cur = set(t[i].split(","))
        num_set = cur - prev_set
        prev_set = cur
        answer.append(int(num_set.pop()))
    return answer
