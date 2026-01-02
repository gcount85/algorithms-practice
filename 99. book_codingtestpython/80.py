# 거스름돈 주기
# [1, 10, 50, 100]


def solution(amount):
    change = [1, 10, 50, 100]
    change.sort(reverse=True)
    answer = []
    for c in change:
        if amount == 0:
            break
        share = amount // c
        amount %= c
        answer.extend([c] * share)
    return answer


print(solution(123))
print(solution(350))
