# 출처: https://chanhuiseok.github.io/posts/baek-1/
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


def promising(r):        # 탐색행번호    ## 0~i-1까지의 col과 각각 비교해야 함!!
    for i in range(r):   # r 행 윗부분 탐색
        if array[r] == array[i]:  # 같은 열에 놓인 퀸이 있으면
            return False
        elif (abs(r-i)) == (abs(array[r]-array[i])):  # 대각선이면
            return False
    return True


def queen(r):  # 행
    global count
    if r == N:   # 마지막 행에 도달하면 경우의 수 +1
        count += 1
        return
    for col in range(N):  # r행의 각각의 컬럼에 대해서 퀸 두기
        array[r] = col
        if promising(r) == True:
            queen(r+1)


N = int(sys.stdin.readline())
array = [0] * N  # [0, 0, 0, 0, 0, 0, 0, 0] 각 인덱스는 i행을 의미, 원소값은 i행의 열 번호를 의미
count = 0

queen(0)
print(count)

# ## 체스두기
# 해당 인덱스에 체스 둠(해당 열 번호를 위치[행]에 넣어줌)
# if 끝 행까지 갔으면 재귀 종료
# if 가능성 판단 함수 not none
# 	체스두기(가능성 판단 함수가 준 인덱스 리턴값)
