from sys import stdin

n = int(stdin.readline())
mtx = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]

answer = {-1: 0, 0: 0, 1: 0}

def check(n, s, e):
    for i in range(n): # 0~8
        for j in range(n): # 0~8
            if mtx[s+i][e+j] != mtx[s][e]:
                return False
    return True

def solution(n, s, e): # 행 길이, 시작 행, 시작 열 
    mark = mtx[s][e]
    if check(n, s, e):
        answer[mark] += 1
        return
    
    for k in range(3): # 0, 1, 2 에다가 n//3을 곱함
        for l in range(3): 
            solution(n//3, s + n//3*k, e + n//3*l)

solution(n, 0, 0)
print(answer[-1], answer[0], answer[1])

# 출력
# -1로만 채워진 종이의 개수
# 0으로만 채워진 종이의 개수
# 1로만 채워진 종이의 개수

