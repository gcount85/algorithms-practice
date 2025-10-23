"""
https://school.programmers.co.kr/learn/courses/30/lessons/76502
- 괄호 문자열을 왼쪽으로 x칸 shift 했을 때, s가 올바른 괄호 문자열이 되게 하는 x의 개수 (0 ~ s의 길이-1)
- s는 1000개 -> O(N^2)까지
"""


def solution(s):
    """
    - [반복문] i = 0부터 len(s)까지 반복문
        - 스택을 만든다.
        - [반복문] i부터 i + len(s)까지 반복문
            - i > len(s)이면 두개 뺀 거 절대값을 구함
            - 문자열의 i번 인덱스부터 스택에 집어넣는다.
                - 열린 괄호면 집어넣는다.
                - 닫힌 괄호면 스택을 pop한다. (단 pop 원소가 열린 괄호랑 짝이 맞으면!)
        - 스택이 비어있으면 정답 횟수 증가, 아니면 다음 반복 진행
    """

    answer = 0
    n = len(s)
    for i in range(0, n):
        stack = []
        # print(i)
        for j in range(i, i + n):  # 1 ~ 6
            index = j  # 6
            # print(j)

            if j >= n:
                index = j - n  # index = 6 - 6 = 0
            b = s[index]
            # print(b)

            if b in ["]", ")", "}"] and len(stack) == 0:
                stack.append("fail")
                break

            if b in ["[", "(", "{"]:
                stack.append(b)
                continue
            else:
                if not stack:
                    stack.append("fail")
                    break

            if b == "]" and stack[-1] == "[":
                stack.pop()
            elif b == ")" and stack[-1] == "(":
                stack.pop()
            elif b == "}" and stack[-1] == "{":
                stack.pop()
            else:
                break
        # print(stack)
        if len(stack) == 0:
            answer += 1
    return answer
