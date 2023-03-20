# 60점
def solution(numbers):
    if sum(numbers) == 0:
        return "0"
    string = list(map(str, numbers))
    string.sort(key=lambda x: (x[0], x[-1]), reverse=True)
    # print(string)
    return "".join(string)


# 100점
def solution(numbers):
    if sum(numbers) == 0:
        return "0"
    string = list(map(str, numbers))
    string.sort(key=lambda x: x * 3, reverse=True)  # x * 3이 포인트
    # print(string)
    return "".join(string)
