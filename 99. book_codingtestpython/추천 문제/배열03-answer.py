# https://school.programmers.co.kr/learn/courses/30/lessons/87390
# (i,j) 칸에 들어가는 숫자는 그 칸이 속한 ‘큰 번호(행/열)’의 번호 + 1이다.


def solution(n, left, right):
    ans = []
    for k in range(left, right + 1):
        i, j = divmod(k, n)  # 몫, 나머지 = 행, 열
        ans.append(max(i, j) + 1)
    return ans
