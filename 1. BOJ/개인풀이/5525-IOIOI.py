# 100점 (O(N))
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

def check_pattern(s, n):
    count = 0
    consecutive_ioi = 0
    i = 0

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

print(check_pattern(s, n))


# def check_pattern(l, h):
#     tmp_l, tmp_h = l, h
#     while tmp_l <= tmp_h:
#         ioi = 'I'
#         if (tmp_l - l) % 2 == 1:
#             ioi = 'O'
#         if s[tmp_l] != s[tmp_h]:
#             return False
#         if s[tmp_l] != ioi or s[tmp_h] != ioi:
#             return False
#         tmp_l += 1
#         tmp_h -= 1
#     return True
    

# l, h = 0, 2 * n
# count = 0
# while h < m:
#     if check_pattern(l, h):
#         # print(s[l:h+1])
#         count += 1
#         l += 2
#         h += 2
#     else:
#         l += 1
#         h += 1
    
# print(count)



