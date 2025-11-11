"""
https://school.programmers.co.kr/learn/courses/30/lessons/131127#
일정한 금액을 지불하면 10일 동안 회원 자격을 줌
회원을 대상으로 매일 한 가지 제품을 할인받음
할인하는 제품은 하루에 하나씩만 구매
내가 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입
discount 길이 10만개 -> NlogN
"""


def solution(want, number, discount):
    """
    - (k,v = want,number)인 딕셔너리 생성
    - discount 배열에서 인덱스로 슬라이딩 윈도우, size는 number의 sum => 0 ~ sum-1 부터 시작
    - 윈도우 사이즈 내의 원소를 순회:
        want dict에서 발견되면 --v
    - 다 순회하고 want dict items의 sum이 0 이하이면 ++count

    - [반복] sum-1이 discount 마지막 인덱스가 될 때까지
        - 포인터를 옮기면서, 삭제되는 품목은 want dict에서 ++1, 추가 되는 품목은 want dict에서 --1
        - want dict items의 sum이 0 이하이면 ++count
    """
    dic = {}
    for w, n in zip(want, number):
        dic[w] = n
    sum_number = sum(number)
    start = 0
    end = sum_number - 1

    # print(sum_number, start, end)

    for i in range(end + 1):
        discount_elem = discount[i]
        if discount_elem in dic:
            dic[discount_elem] -= 1

    answer = 0
    for v in dic.values():
        if v > 0:
            break
    else:
        answer += 1

    while end + 1 < len(discount):  # O(N) discount 개수 N
        start += 1
        end += 1
        deleted_elem = discount[start - 1]  # 윈도우 옮기면서 제외 되는 할인 품목
        added_elem = discount[end]  # 윈도우 옮기면서 추가되는 할인 품목

        # 제외되고 추가되는 애들 업데이트
        if deleted_elem in dic:
            dic[deleted_elem] += 1
        if added_elem in dic:
            dic[added_elem] -= 1

        if deleted_elem in dic and dic[deleted_elem] > 0:
            continue
        if added_elem in dic and dic[added_elem] > 0:
            continue

        if all(v <= 0 for v in dic.values()):
            answer += 1
        # print(start, end, dic, answer)

    return answer
