# https://www.acmicpc.net/problem/9935 문자열 폭발

## 못 풀었습니다;;


import sys
from collections import deque

# main_str = list(sys.stdin.readline().strip())
# boom_str = list(sys.stdin.readline().strip())
# main_string = ['m','i','r','k','o','v','C','4','n','i','z','C','C','4','4']
main_string = 'mirkovC4nizCC44'
# boom_str = ['C', '4']
boom_str = 'C4'
stack0 = deque()
stack1 = deque()
boom_count = 0

while boom_count != 0:
    for i in main_string:
        if i == boom_str[0]:
            stack1.append(i)
        stack0.append(i)







