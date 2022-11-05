import sys

def stack_structure(stack: list):
    count = 1
    std = stack[-1]
    stack.pop()
    while len(stack) != 0:
        if stack[-1] <= std:
            stack.pop()
        elif stack[-1] > std:
            count += 1
            stack.pop()
    print(count)

stack = []
N = int(sys.stdin.readline())

# 입력받기
for _ in range(N):
    input = int(sys.stdin.readline())
    stack.append(input)

stack_structure(stack)