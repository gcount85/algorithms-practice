# https://www.acmicpc.net/problem/1107
# 그리디 방식으로 풀었으나 정확하지 않음. 완전 탐색으로 다시 풀이 

from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
if m != 0:
    btns = list(map(int, stdin.readline().strip().split()))
else:
    btns = None

def solution(n, btns):
    if n == 100:
        return 0
    if not btns or not [btn for btn in btns if str(btn) in str(n)]:
        return min(abs(100-n), len(str(n)))
    
    pointer = 0
    candid = [None] * len(str(n)) 
    while pointer < len(str(n)):
        num = int(str(n)[pointer])
        tmp = []
        for b in range(10):
            if b not in btns:   # i가 누를 수 있는 버튼이면 
                tmp.append([abs(num-b), b])
                tmp.append([abs(num+10-b), b])
        tmp.sort()
        candid[pointer] = [tmp[0][1], tmp[1][1]]
        pointer += 1

    # print(tmp)
    # print(candid)

    num0, num1 = "", ""
    for p, digit in enumerate(candid):
        if p == 0 and digit[0] == 10:
                digit[0] = "10"
        if p == 0 and digit[1] == 10:
                digit[1] = "10"
        num0 += str(digit[0])
        num1 += str(digit[1])

    # print(num0, num1)
    return min(abs(int(num0)-n) + len(num0), abs(int(num1)-n) + len(num1))


print(solution(n, m, btns))

    


"""
1. 채널은 양의 정수
2. 디폴트 채널은 100번 


"""