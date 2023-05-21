# https://www.acmicpc.net/problem/1107
# 완전탐색

from sys import stdin

# 채널에 고장난 버튼이 있는지 확인 및 자리수 계산 
def check(channel):
    if channel == 0:
        if broken[0]:
            return 0
        else:
            return 1
    length = 0
    while channel > 0:
        if broken[channel % 10]:
            return 0
        length += 1
        channel //= 10
    return length


N = int(stdin.readline())
M = int(stdin.readline())
broken = [0] * 10

a = list(map(int, stdin.readline().split())) if M > 0 else []

# 망가진 버튼 표시 
for x in a:
    broken[x] = 1

min_cnt = abs(100 - N)

for c in range(900001):  # 50만까지 체크하면 틀림! 
    length = check(c)
    if length > 0:
        press = abs(c - N)
        min_cnt = min(min_cnt, length + press)

print(min_cnt)



"""
1. 채널은 양의 정수
2. 디폴트 채널은 100번 


"""