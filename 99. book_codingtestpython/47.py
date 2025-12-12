def backtrack(sum, selected_nums, start, N, results):
    if sum == 10:
        results.append(selected_nums)
        return

    for i in range(start, N + 1):
        if sum + i <= 10:
            backtrack(sum + i, selected_nums + [i], i + 1, N, results)


def solution(N):
    results = []
    backtrack(0, [], 1, N, results)
    return results


print(solution(5))
