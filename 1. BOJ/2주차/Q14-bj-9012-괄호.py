import sys

def stack_structure(input: str):
    stack = []
    for i in input:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()  
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


N = int(sys.stdin.readline())

# input = "()()()()(()()())()"  #yes
# input = "(()())((()))" ## yes
# input = "())(()" ## no
# input = "((" ## no
# print(stack_structure(input))


for _ in range(N):
    input = sys.stdin.readline().strip()
    # print(input)
    print(stack_structure(input))
