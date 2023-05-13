from collections import deque
import timeit


def my_solution(N):
    stack = deque()
    gap = 0

    # Convert decimal number 10 into binary
    binary_num = bin(N)[2:]

    for i in binary_num:
        if i == '1' and len(stack) != 0:
            temp_gap = 0
            while stack[-1] != '1':
                stack.pop()
                temp_gap += 1
            gap = max(gap, temp_gap)
        stack.append(i)

    return gap


# Elapsed time: 0.0028549000000000005 seconds
def best_solution(N):
    binary_num = bin(N)[2:]
    max_gap = 0
    temp_gap = 0

    for i in binary_num:
        if i == 0:
            temp_gap += 1
        else:
            max_gap = max(temp_gap, max_gap)
            temp_gap = 0

    return max_gap


N = 101000230345

# Run the function 1000 times
elapsed_time1 = timeit.timeit(lambda: my_solution(N), number=1000)
print(f"Elapsed time: {elapsed_time1} seconds")

elapsed_time2 = timeit.timeit(lambda: best_solution(N), number=1000)
print(f"Elapsed time: {elapsed_time2} seconds")


'''
리턴:
주어진 N을 이진 수로 바꿨을 때, 1로 감싸진 0의 최대 길이 
없으면 0

범위:
[1..2147483647] =  2의 31승 -1

예외:
1) 시작하는 1과 끝나는 1이 있어야 함


'''
