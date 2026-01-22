# 1000만 -> O(N), 10만 -> ONlogN
# https://school.programmers.co.kr/learn/courses/30/lessons/87390


def solution(n, left, right):
    start_row = left // n
    end_row = right // n
    new_list = []
    for i in range(start_row, end_row + 1):
        for j in range(n):
            if j <= i:
                new_list.append(i + 1)
            else:
                new_list.append(j + 1)
    return new_list[left % n : ((end_row - start_row) * n) + (right % n) + 1]
