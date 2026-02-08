# https://school.programmers.co.kr/learn/courses/30/lessons/17686#
# 시간 복잡도 O(N*M)


def solution(files):
    """
    1. 해시 테이블로 원래 파일명, 정규화 파일명으로 분리(split, tuple)
    2. value 기준으로 정렬 후, 해시 테이블 순회하면서 key를 출력
    """

    answer = []
    for f in files:  # O(N)
        head = []
        number = []
        head_end = number_end = False
        for ch in f:  # O(M)
            if ch.isalpha() and not head_end:
                head.append(ch)
            elif ch.isdigit() and not head_end:
                head_end = True
                number.append(ch)
            elif ch.isdigit() and head_end and len(number) < 5:
                number.append(ch)
            elif ch.isalpha() and not number_end:
                number_end = True
                break
            elif not head_end:
                head.append(ch)
        head = "".join(head).lower()  # O(M)
        number = int("".join(number))  # O(M)
        answer.append((head, number, f))

    sorted_map = sorted(answer, key=lambda x: (x[0], x[1]))
    return [el[2] for el in sorted_map]
