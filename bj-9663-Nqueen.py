# 출처: https://chanhuiseok.github.io/posts/baek-1/

# 퀸을 놓는 과정을 재귀적으로 구현하고, 위처럼 1차원 배열만을 활용하여 다시 구현
import sys

# start 인덱스부터 시작 
# 퀸의 위치를 알려주는 배열 생성(0부터 n-1까지의 인덱스를 가진)

# ## 가능성 판단 함수  
# 다음 위치부터 끝까지
# 조건: 이 자리에 놓을 수 있는가?
# 	스타트와 같은 행이면 안됨	
# 	스타트와 같은 열이면 안됨
# 	스타트와 대각선 위치면 안됨(대각선인걸 어떻게 알것인가?)
# 	안되면 return;
# 	되면 return 열 인덱스 반환 (원래행+1, 열)
N = int(sys.stdin.readline())
# N = 8
array = [0] * N   ## [0, 0, 0, 0, 0, 0, 0, 0] 각 인덱스는 i행을 의미, 원소값은 i행의 열 번호를 의미  
c = 0

def promising(r):               #탐색행번호    ## 0~i-1까지의 col과 각각 비교해야 함!! 
    for i in range(r):          #0부터 r-1까지의 행번호
        if array[r] == array[i]:   # 같은 열이면(수직이면)
            return False
        elif (abs(r-i)) == (abs(array[r]-array[i])): ## 대각선이면
            return False
    return True

def queen(r):  #행, c
    global c
    if r == N:   #행번호가 끝번호면
        c += 1
        return
    else:
        for col in range(N):
            array[r] = col
            if promising(r):   #이거 트루로 하면 안댐!!! 
                queen(r+1)

queen(0)
print(c)
# print(위치)

# ## 체스두기 
# 해당 인덱스에 체스 둠(해당 열 번호를 위치[행]에 넣어줌)
# if 끝 행까지 갔으면 재귀 종료 
# if 가능성 판단 함수 not none
# 	체스두기(가능성 판단 함수가 준 인덱스 리턴값)








