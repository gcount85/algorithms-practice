# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 16분 solved

"""
- 한 번호가 다른 번호의 접두어인지 확인
- 접두어가 있으면 false, 없으면 true
- n은 100만 -> nlogn 이하
- 번호 중복 X
"""


def solution(phone_book):
    phone_set = set(phone_book)  # O(N)
    for p in phone_book:  # O(N*M)
        for i in range(1, len(p)):
            if p[0:i] in phone_set:
                return False
    return True


"""
빅O 상으로는 pass2보다 빠를 거 같지만 느림. 
because
    1) 접두어 슬라이스로 새 문자열을 엄청 많이 생성
    2) 각 전화번호 p에 대해 접두어를 전부 만들어서 set에 있는지 확인 => 불필요한 해시 조회 큼
    3) 메모리/GC 비용도 큼
반면 pass1은
    1) 반복문에서 비교 횟수가 N-1로 고정
    2) startswith는 할당 없이 비교만 함 => 문자열 생성 X


"""
