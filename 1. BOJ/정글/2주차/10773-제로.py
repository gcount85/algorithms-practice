# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 
# 가장 최근에 재민이가 쓴 수를 지우게 시킨다. (pop한다)
# 재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 


import sys 

stack = []

def stack_structure(input: int):
    global stack
    if input == 0:
        stack.pop() ## print 씌워주어야 출력 됨
    else:
        stack.append(input)

N = int(sys.stdin.readline())

for _ in range(N):
    input = int(sys.stdin.readline())
    # print(input)
    stack_structure(input)


print(sum(stack))




    


