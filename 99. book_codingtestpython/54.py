def solution(string):
    ordered = [0] * 27
    for a in string:
        ordered[ord(a) - ord("a")] += 1

    answer = []
    for i, v in enumerate(ordered):
        answer.append(chr((ord("a") + i)) * v)

    return "".join(answer)


print(solution("hello"))  # ehllo
print(solution("algorithm"))  # aghilmort
