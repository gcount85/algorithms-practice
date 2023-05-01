# 50점

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

def check_pattern(l, h):
    tmp_l, tmp_h = l, h
    while tmp_l <= tmp_h:
        ioi = 'I'
        if (tmp_l - l) % 2 == 1:
            ioi = 'O'
        if s[tmp_l] != s[tmp_h]:
            return False
        if s[tmp_l] != ioi or s[tmp_h] != ioi:
            return False
        tmp_l += 1
        tmp_h -= 1
    return True
    

l, h = 0, 2 * n
count = 0
while h < m:
    if check_pattern(l, h):
        # print(s[l:h+1])
        count += 1
        l += 2
        h += 2
    else:
        l += 1
        h += 1
    
print(count)

''' 
- IOI 형태로 있는지 확인하는 함수
    - 양쪽 끝 문자가 I가 아니면 pass 
    - 양쪽에서 두 번째 문자들이 O가 아니면 pass
    - 양쪽에서 세번째 문자열의 인덱스가 
- m부터 길이 3까지만 확인 (p1은 길이 3부터이므로)
- 찾고자 하는 값은 길이가 m일때의 dp 값  
- 길이가 n일때의 dp값은 ? 

'''



