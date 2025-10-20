"""
- 괄호를 순서대로 스택에 담는다
- 담다가, 닫힌 괄호를 만나면 pop 한다.
- 반복하다가 마지막에 스택에 원소가 0 이상이면 false, 아니면 true

"""


def solution(brackets):
    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
            continue
        stack.pop()
    if len(stack) > 0:
        return False
    return True


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution("(())()"))  # 반환값 : True
print(solution("((())()"))  # 반환값 : False
print(solution("()()((()()))()((()))(((((())))))"))  # 반환값 : True
