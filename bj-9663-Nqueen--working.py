# 출처: https://chanhuiseok.github.io/posts/baek-1/

# 퀸을 놓는 과정을 재귀적으로 구현하고, 위처럼 1차원 배열만을 활용하여 다시 구현
import sys

# N = int, sys.stdin.readline()
N = 8
위치 = [0] * N   ## [0, 0, 0, 0, 0, 0, 0, 0] 각 인덱스는 i행을 의미, 원소값은 i행의 열 번호를 의미  
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

def 가능성판단(i, x):  #행번호, 열번호
    내위치 = 위치[i]
    for j in range(i+1, N):      ## 행 번호 
        내dec값 = i*N+내위치
        for k in range(0, N):  ## 열번호 
            탐색dec값 = j*N+k
            if k == x:  ## 같은 열이면(수직이면)
                continue
            elif (abs((내dec값)-(탐색dec값)) == N-1) or (abs((내dec값)-(탐색dec값)) == N+1): ## 대각선이면
                continue 
            # else:
                # return j, k
        return j, k

c = 0
def 퀸두기(j, k, c):
    if j == N:  #행번호가 끝번호면
        c += 1 
        return c  #경우의 수 반환
    if 가능성판단(j, k):
        행, 열 = 가능성판단(j, k)
        위치[행] = 열
        return 퀸두기(행, 열, c)

퀸두기(0, 0, c)
print(c)

# ## 체스두기 
# 해당 인덱스에 체스 둠(해당 열 번호를 위치[행]에 넣어줌)
# if 끝 행까지 갔으면 재귀 종료 
# if 가능성 판단 함수 not none
# 	체스두기(가능성 판단 함수가 준 인덱스 리턴값)








