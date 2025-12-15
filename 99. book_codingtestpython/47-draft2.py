# 3시 10분 시작

"""
1. 1부터 10까지 반복
    1-1. 숫자 선택
    1-2. selected_num에 추가
    1-3. 합을 구한다:
        10이면: answer 배열에 추가, return True
        10이 넘으면: return False
        10 미만이면: keep going

"""


def solution(N):

    answer = []

    def dfs(N, num, total, selected_nums):
        for i in range(num, N + 1):
            selected_nums.append(i)
            new_total = total + i
            if new_total == 10:
                answer.append(selected_nums[:])
                selected_nums.pop()
                continue
            if new_total > 10:
                selected_nums.pop()
                continue
            dfs(N, i + 1, new_total, selected_nums)
            selected_nums.pop()

    dfs(N, 1, 0, [])
    return answer


print(solution(5))
print(solution(2))
print(solution(7))
