# https://school.programmers.co.kr/learn/courses/30/lessons/17684


def solution(msg):
    """
    0. 색인번호 초기화(27), 딕셔너리 초기화: (k,v) = (단어,색인번호)
    1. [while 반복] until 글자 끝까지 닿을 때까지 (현재글자포인터, 다음글자 포인터)
        1-1. 현재 글자 + 다음 글자가 사전에 있어?:
            1-1-1. 그 다음글자까지 end 포인터 넘김
        1-2. 없어:
            1-2-1. 이전 글자까지 색인 출력
            1-2-2. 현재글자 + 다음 글자를 사전에 넣음
    """

    dic = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }
    index = 27
    start = 0
    end = 1
    n = len(msg)
    answer = []
    while True:
        target = msg[start : end + 1]
        if target in dic:
            end += 1
            if end >= n:
                answer.append(dic[target])
                break
        else:
            answer.append(dic[target[:-1]])
            dic[target] = index
            index += 1
            start = end
            end += 1

    return answer
