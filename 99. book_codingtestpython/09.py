"""
- [반복] 주어진 숫자를 2로 나누는데, 몫이 0이 될때까지 나눔
    - 이때 발생한 나머지를 스택에 담음
- 스택 원소를 모두 pop 해서 나열하면 됨

"""


def solution(num):
    stack = []
    while num // 2 != 0:  # logN
        stack.append(str(num % 2))
        num //= 2
    stack.append("1")
    stack.reverse()
    return "".join(stack)

    # stack.reverse()를 사용하면 아래는 안 해도 된다.
    # answer = []
    # for i in range(1, len(stack) + 1):
    #     answer.append(stack[-i])
    # stack.reverse()
    # return "".join(answer)


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution(10))  # 반환값 :  1010
print(solution(27))  # 반환값 :  11011
print(solution(12345))  # 반환값 : 11000000111001

# 10 / 2 = 5 .. 0
# 5 / 2 = 2 .. 1
# 2 / 2 = 1 .. 0
# 1 / 2 = 0 .. 1

# 27 / 2 = 13 .. 1
# 13 / 2 = 6 .. 1
# 6 / 2 = 3 .. 0
# 3 / 2 = 1 .. 1
# 1 / 2 = 0 .. 1
