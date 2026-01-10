# https://school.programmers.co.kr/learn/courses/30/lessons/77886


def solution(s):
    """
    1. 스택으로 110을 제거 및 카운팅
    2. 뒤에서부터 0을 찾아서, 0 뒤에 110*count 삽입
    """

    answer = []

    for string in s:

        # 110 제거 및 카운팅
        stack = []
        count = 0
        for elem in string:
            stack.append(elem)
            if len(stack) >= 3 and stack[-3:] == ["1", "1", "0"]:
                stack.pop()
                stack.pop()
                stack.pop()
                count += 1

        # 마지막 0 위치인 i 찾기
        p = len(stack) - 1
        while p >= 0:
            if stack[p] == "0":
                break
            p -= 1

        # 문자열 조합
        lst = stack[: p + 1]
        lst.extend(["1", "1", "0"] * count)
        lst.extend(stack[p + 1 :])
        answer.append("".join(lst))

    return answer
