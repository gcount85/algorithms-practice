# https://school.programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    """
    1. record 를 순회하면서 딕셔너리 만듦 (k, v = uid, 닉넴)
        1-1. leave 인 경우를 제외하고, uid, 닉넴을 딕셔너리에 업뎃
    2. record를 순회
        2-1. change인 경우를 제외하고 메시지 출력
    """

    dic = {}
    for r in record:
        if r.startswith("Leave"):
            continue
        _, uid, name = r.split(" ")
        dic[uid] = name

    answer = []
    for r in record:
        if r.startswith("Change"):
            continue
        splited = r.split(" ")
        action = splited[0]
        uid = splited[1]
        name = dic[uid]
        msg = (
            f"{name}님이 들어왔습니다."
            if action == "Enter"
            else f"{name}님이 나갔습니다."
        )
        answer.append(msg)

    return answer
