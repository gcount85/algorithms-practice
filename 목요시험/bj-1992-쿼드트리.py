# https://www.acmicpc.net/problem/1992 쿼드트리 

# print(spots)
# size_N = 8
# spots = [[1,1,1,1,0,0,0,0],
#         [1,1,1,1,0,0,0,0],
#         [0,0,0,1,1,1,0,0],
#         [0,0,0,1,1,1,0,0],
#         [1,1,1,1,0,0,0,0],
#         [1,1,1,1,0,0,0,0],
#         [1,1,1,1,0,0,1,1],
#         [1,1,1,1,0,0,1,1]]

'''        
슈도코드
1~4분면에 대해 모두 1 or 0인지 확인
    여는 괄호 어펜드
    모두 1이면 출력에 1추가
    모두 0이면 출력에 0추가
    사분면 체크가 끝나면 괄호 append
아니면
    N/2 × N/2spots로 나누기
이걸 반복w
출력 = print_list
'''

import sys

size_N = int(sys.stdin.readline())
spots = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(size_N)]
        
# 출력결과 담을 print_list
print_list = ""

# 쿼드트리 체크하는 함수
# 필요한 매개변수: 다차원 리스트 spots, size_N, 시작하는 행, 열번호 srow, scol
def check(spots: list, size_N: int, srow: int, scol: int):
    global print_list
    if size_N == 1:
        if spots[srow][scol] == 1:
            print_list += '1'
        else:
            print_list += '0'
    else:  # 사이즈 2, 4, 8 ... 일때 
        temp0 = 0
        temp1 = 0
        for i in range(srow, srow+size_N): #0,1,2,3
            for j in range(scol, scol+size_N):  #0,1,2,3
                if spots[i][j] == 1:
                    temp1 += 1
                else:
                    temp0 += 1
        if temp1 == size_N**2:
            print_list += '1'
        elif temp0 == size_N**2:
            print_list += '0'
        else:
            mrow, mcol = srow + (size_N//2), scol + (size_N//2)
            print_list += "("
            check(spots, size_N//2, srow, scol)  # 1사분면체크  scol, srow를 0으로 지정해서 오류났었다!
            check(spots, size_N//2, srow, mcol)  # 2사분면체크
            check(spots, size_N//2, mrow, scol)  # 3사분면체크
            check(spots, size_N//2, mrow, mcol)  # 4사분면체크
            print_list += ")"

check(spots, size_N, 0, 0)
print(print_list)