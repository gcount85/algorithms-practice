"""
https://school.programmers.co.kr/learn/courses/30/lessons/42889
전체 스테이지 개수 N: 1~500
현재 사람들이 멈춰있는 스테이지의 번호 배열 stages: 1~200,000 (20만)
    - N+1은 마지막 스테이지(N스테이지)까지 클리어한 사용자의 수
    - 다음 단계의 스테이지로 갈 수록 분모(도전 사용자)에서 이전 단계의 실패 사용자(이전 단계의 분자)를 빼야 함
    - N+1 단계의 사용자는 1단계 도전자 수 계산할 때에만 포함.
실패율이 높은 스테이지부터 내림차순으로 스테이지 번호 배열 return
    - 실패율이 같은 애들끼리는 스테이지 번호를 오름차순으로 정렬
"""


def solution(N, stages):
    """
    - v [반복문] stages를 순회하며 각 단계에 몇 명이 머물고 있는지 계산
    - 마지막 단계 도전자 수를 저장(초기값은 전체 도전자)
    - [반복문] N 번 반복하며, 각 N 단계의 실패율을 계산
        - 각 단계의 실패율 = 스테이지에 머무는 도전자 수/막단계 도전자 수
        - 스테이지에 머무는 도전자 수는 배열에서 N의 개수
        - 막 단계 도전자 수에서 스테이지에 머무는 도전자 수를 뺄셈
    - 실패율 기준으로 스테이지 번호 내림차순 & 실패율 같으면 스테이지 번호는 오름차순으로 이중 정렬

    """

    # N = 2 이고, stages가 [1, 1, 1, 1, 1, 1]
    nums = [0] * (N + 2)
    for v in stages:  # O(N)
        nums[v] += 1

    last_num = len(stages)
    fail_dict = {}
    for i in range(1, N + 1):  # O(N)
        if last_num == 0:
            fail_dict[i] = 0
        else:
            fail_rate = nums[i] / last_num
            fail_dict[i] = fail_rate
        last_num -= nums[i]

    # 정렬 O(NlogN), zip O(N)
    # sort_answer = sorted(fail_dict.items(), key=lambda x: (-x[1], x[0]))
    # answer, values = zip(*sort_answer)

    # dict는 keys를 순회하므로 아래처럼 쓰는 게 가능하다!
    answer = sorted(fail_dict, key=lambda x: fail_dict[x], reverse=True)
    return answer
