# https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 25분 solved

"""
유저는 한 번에 한 명의 유저를 신고
무제한 신고 가능
중복 신고는 X -> set 사용
k번 이상 신고 누적시 해당 유저 계정 정지 & 해당 유저를 신고한 모든 유저에게 메일 보냄
유저마다 메일을 몇번 받았는지 횟수 배열 반환

"""


def solution(id_list, report, k):
    """
    1. 신고 딕셔너리 만듦. k, v = 신고 받은 유저, (신고 누적 횟수, [해당 유저를 신고한 유저])
    2. 메일링 횟수 딕셔너리를 만듦. k, v = 유저, 메일받은 횟수
    3. 신고 딕셔너리 k, v를 순회:
        2-1. 신고 누적횟수를 초과?: 신고한 유저들의 메일링 딕셔너리 ++1
    4. id_list 순회하면서 메일링 딕셔너리 값 반환

    """
    unique_report = set(report)  # O(N)
    report_dic = {}
    for e in unique_report:  # O(N)
        former, latter = e.split(" ")  # former 신고자, latter 신고 받은 애
        if latter not in report_dic:
            report_dic[latter] = [1, [former]]
        else:
            report_dic[latter][0] += 1
            report_dic[latter][1].append(former)

    mail_dic = {}
    for total, reporter_list in report_dic.values():  # O(N)
        if total >= k:
            for r in reporter_list:
                if r not in mail_dic:
                    mail_dic[r] = 1
                else:
                    mail_dic[r] += 1
    answer = []
    for e in id_list:  # O(M)
        answer.append(mail_dic.get(e, 0))

    return answer
