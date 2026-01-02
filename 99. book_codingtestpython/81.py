# 거스름돈 주기
# [1, 10, 50, 100]


def solution(items, weight_limit):
    items.sort(key=lambda x: -(x[1] / x[0]))  # 무게, 가치
    answer = 0
    for weight, value in items:
        diff = weight_limit - weight
        if diff <= 0:  # 무게 모두 소진
            answer += value / weight * weight_limit
            break
        answer += value
        weight_limit = diff

    return answer


print(solution([[10, 19], [7, 10], [6, 10]], 15))
print(solution([[10, 60], [20, 100], [30, 120]], 50))
