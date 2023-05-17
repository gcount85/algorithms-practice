# https://www.acmicpc.net/problem/1107
from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
if m != 0:
    btns = list(map(int, stdin.readline().strip().split()))
else:
    btns = None

def solution(n, m, btns):
    if n == 100:
        return 0
    if not btns or not [btn for btn in btns if str(btn) in str(n)]:
        return min(abs(100-n), len(str(n)))
    
    pointer = 0
    candid = [None] * len(str(n)) 
    while pointer < len(str(n)):
        if (num := int(str(n)[pointer])) in btns:
            (tmp := [[abs(num-i), i] for i in range(11) if i not in btns]).sort()
            candid[pointer] = [tmp[0][1], tmp[1][1]]
        else:
            candid[pointer] = [num]
        pointer += 1

    num0, num1 = "", ""
    for p, digit in enumerate(candid):
        if len(digit) == 2:
            if p > 0 and digit[0] == 10:
                digit[0] = "0"
            if p > 0 and digit[1] == 10:
                digit[1] = "0"
            num0 += str(digit[0])
            num1 += str(digit[1])
        else: 
            num0 += str(digit[0])
            num1 += str(digit[0])

    # print(num0, num1)
    return min(abs(int(num0)-n) + len(num0), abs(int(num1)-n) + len(num1))


print(solution(n, m, btns))

    


"""
1. 채널은 양의 정수
2. 디폴트 채널은 100번 


"""