# https://school.programmers.co.kr/learn/courses/30/lessons/70129


def solution(s):
    """
    1. 다음을 반복 until s == 1
        1. s의 길이 측정
        2. s에서 0을 제거
        3. 제거한 후의 s의 길이를 측정
        4. s = 현재 s의 길이를 이진수로 바꾼 값
    """

    count = 0
    zero = 0
    while s != "1":
        before_len = len(s)
        s = s.replace("0", "")
        after_len = len(s)
        zero += before_len - after_len
        s = format(after_len, "b")
        count += 1
    return [count, zero]
