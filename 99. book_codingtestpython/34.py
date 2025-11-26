# https://school.programmers.co.kr/learn/courses/30/lessons/1845

"""
- 총 N 마리 중 N/2마리 가져감
- 포켓몬 중복 허용
- 최대한 많은 종류의 포켓몬 가지고 싶음
- N은 만개, 포켓몬 종류는 20만 => nlogn 이하로
"""


def solution(nums):
    """
    1. 포켓몬 배열을 집합에 넣어서 중복을 없앤다.
    2. 중복을 없앤 배열의 개수를 세서 포켓몬이 몇 종류 있나 센다(예. 3종류, 2종류)
    3. 만약에 중복을 없앴는데 n/2보다 큰가?:
        3-1. 정답은 n/2
        3-2. 작다면 중복을 없앤 배열의 개수가 정답
    """
    n = len(nums)
    unique_set = set(nums)
    unique_len = len(unique_set)
    return min(unique_len, int(n / 2))
