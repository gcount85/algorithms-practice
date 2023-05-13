# 100점 (O(N))
from sys import stdin

def check_pattern(s: str, n):
    i = s.find("IOI")
    if (i == -1):
        return 0

    consecutive_ioi = 0
    count = 0

    while i < len(s) - 2:
        if s[i:i+3] == "IOI":
            consecutive_ioi += 1
            if consecutive_ioi == n:
                count += 1
                consecutive_ioi -= 1 # 중복 패턴 카운트 
            i += 2
        else:
            consecutive_ioi = 0
            i += 1

    return count

n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline().strip()

print(check_pattern(s, n))
