# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 2021년 1월 5일 수집 -> 12개월 유효기간 -> 2022년 1월 4일까지 보관, 1월 5일부터 파기.
# 모든 달은 28일까지만 있음
# 파기할 개인정보 번호를 오름차순 정렬리턴


def to_days(date):
    y, m, d = map(int, date.split("."))
    return y * 12 * 28 + m * 28 + d


def solution(today, terms, privacies):
    terms_dic = {elem.split(" ")[0]: int(elem.split(" ")[1]) for elem in terms}
    todays = to_days(today)
    answer = []

    for i, p in enumerate(privacies):
        date, term = p.split(" ")
        expire_days = to_days(date) + terms_dic[term] * 28
        if todays >= expire_days:
            answer.append(i + 1)
    return answer
