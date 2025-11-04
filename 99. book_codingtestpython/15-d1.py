"""
- 1부터 N까지 번호표
- 1번 기준으로 k 번째 사람 제거
"""


def solution(N, K):
    survived = [1 for _ in range(N)]
    start = 0
    to_delete = start + K
    answer = 0
    while True:
        survived[to_delete] = 0
        start = (to_delete + 1) % N
        if survived[start] == 0:
            answer = (to_delete - K) % N
            break
        to_delete = (start + K) % N
        if survived[to_delete] == 0:
            answer = (start - K) % N
            break
    print(survived, "start = ", start + 1, "to_delete", to_delete + 1)
    return answer + 1


print(solution(5, 2))
