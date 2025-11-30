# https://school.programmers.co.kr/learn/courses/30/lessons/42577

"""
- 한 번호가 다른 번호의 접두어인지 확인
- 접두어가 있으면 false, 없으면 true
- n은 100만 -> nlogn 이하
- 번호 중복 X
"""


def solution(phone_book):
    phone_book.sort()  # O(NlogN)
    for i in range(len(phone_book) - 1):  # O(N)
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True
