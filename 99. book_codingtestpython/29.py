# https://school.programmers.co.kr/learn/courses/30/lessons/77486

"""
- 모든 노드는 판매 이익의 10%를 부모 노드에게 주고 나머지 90% 가짐
- 모든 노드는 자식 노드가 벌어들인 추천 포인트의 10%를 쭈루룩 가짐
- 10%를 계산한 금액이 1 원 미만인 경우에는 이득을 분배하지 않고 본인이 가짐

노드 이름 배열 enroll
각 노드의 부모 노드 배열 referral, 루트의 자식은 “-“로 표기
판매량 데이터 노드 이름 seller, 중복 있음
판매량 배열 amount
각 노드의 최종 이익금 배열 return
"""


def solution(enroll, referral, seller, amount):
    """
    1. 트리를 만든다. enroll, referral 가지고. or 딕셔너리?
    2. result 배열을 만든다.
    3. seller, amount 배열을 순회한다
        2-1. amount_won 계산한다 (개수 * 100)
        2-2. 90%는 본인의 돈으로 가짐
        2-3. [반복] 10%의 금액이 1원 미만이 될 때까지
            2-3-1. 부모의 돈으로 더해줌
    """

    referral_dic = dict(zip(enroll, referral))
    result = dict.fromkeys(enroll, 0)
    # result["-"] = 0

    for s, a in zip(seller, amount):
        # 내 돈 저장
        cur = s
        money = a * 100

        # 남길 돈, 넘길 돈을 계산하여 부모들에게 전달
        # ⚠️ 현재 노드 기준에서만 생각하고 부모는 생각 X
        while money >= 1 and cur != "-":
            pass_up = money // 10  # 전달할 10%
            keep = money - pass_up  # 남길 90%
            result[cur] += keep

            cur = referral_dic[cur]
            money = pass_up

            # parent = referral_dic[cur]
            # result[parent] += referral_money
            # cur = parent
            # referral_money = int(referral_money * 0.1)

    # print(result)
    return [result[e] for e in enroll]
