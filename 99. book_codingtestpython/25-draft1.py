# https://school.programmers.co.kr/learn/courses/30/lessons/72411
# 50분 solved

"""
최소 2가지 이상의 단품메뉴로 코스 요리 만든다
가장 많이 주문 된 단품메뉴 조합이면서 최소 2명 이상의 손님이 주문했던 단품메뉴 조합으로만 만든다

"""
from itertools import combinations


def solution(orders, course):
    """
    0. 조합 주문 딕셔너리 만든다. k:v = 조합:누적 주문 수
    1. orders를 순회:
        1-1. course를 순회:
            1-1-1. 묶어야 하는 메뉴 갯수에 따라 조합을 생성(e.g. 2개면 ab, ac, af, ag...)
            1-1-2. 조합 주문 딕셔너리에 ++1 한다.
    2. 조합 주문 딕셔너리를 순회:
        2-1. 값이 2 이상인 것만 배열에 담음
    3. 배열을 (key)로 정렬 한 후 리턴
    """

    order_dic = {}
    for o in orders:
        o = "".join(sorted(o))
        for c in course:
            for combo in combinations(o, c):
                # print(combo)
                joined = "".join(combo)
                if joined not in order_dic:
                    order_dic[joined] = 1
                else:
                    order_dic[joined] += 1

    # print("order_dic", order_dic)
    answer_dic = {}  # k:v = (n: [keys, ...]) n이 c이면서 값이 2 이상인 애들
    max_value = [0] * 11
    for k, v in order_dic.items():
        n = len(k)
        if v < 2:
            continue
        if n not in answer_dic:
            answer_dic[n] = [k]
        else:
            answer_dic[n].append(k)
        max_value[n] = max(max_value[n], v)
    # print("answer_dic", answer_dic)
    answer = []
    for k, v in answer_dic.items():
        for e in v:
            if order_dic[e] == max_value[k]:
                answer.append(e)
    answer.sort()
    return answer
