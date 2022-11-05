# https://www.acmicpc.net/problem/2630

# 첫째 줄에는 전체 종이의 한 변의 길이 N
# N은 2, 4, 8, 16, 32, 64, 128 중 하나
# paper의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다.
# 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.
import sys

size_N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(size_N)]
# print(paper)
# size_N = 8
# paper = [[1, 1, 0, 0, 0, 0, 1, 1],
#         [1, 1, 0, 0, 0, 0, 1, 1],
#         [0, 0, 0, 0, 1, 1, 0, 0],
#         [0, 0, 0, 0, 1, 1, 0, 0],
#         [1, 0, 0, 0, 1, 1, 1, 1],
#         [0, 1, 0, 0, 1, 1, 1, 1],
#         [0, 0, 1, 1, 1, 1, 1, 1],
#         [0, 0, 1, 1, 1, 1, 1, 1]]

paper0 = 0
paper1 = 0
# 필요한 매개변수: 다차원 리스트 paper, size_N 


def check(paper, size_N, srow, scol):
    global paper0, paper1
    if size_N == 1:
        if paper[srow][scol] == 1:
            paper1 += 1
        else:
            paper0 += 1
    else:  # 사이즈 2, 4, 8 ... 일때 
        temp0 = 0
        temp1 = 0
        for i in range(srow, srow+size_N): #0,1,2,3
            for j in range(scol, scol+size_N):  #0,1,2,3
                if paper[i][j] == 1:
                    temp1 += 1
                else:
                    temp0 += 1
        if temp1 == size_N**2:
            paper1 += 1
        elif temp0 == size_N**2:
            paper0 += 1
        else:
            mrow, mcol = srow + (size_N//2), scol + (size_N//2)
            check(paper, size_N//2, srow, scol)  # 1사분면체크  scol, srow를 0으로 지정해서 오류났었다!
            check(paper, size_N//2, srow, mcol)  # 2사분면체크
            check(paper, size_N//2, mrow, scol)  # 3사분면체크
            check(paper, size_N//2, mrow, mcol)  # 4사분면체크
        

# 모두 1 or 0인지 확인
    # 모두 1이면 paper1 += 1
    # 모두 0이면 paper0 += 1
# 아니면
    # N/2 × N/2paper로 나누기
# 이걸 반복

# 출력 = 0 paper 갯수, 1 paper 갯수
check(paper, size_N, 0, 0)
print(paper0, paper1)
