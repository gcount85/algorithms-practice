# https://school.programmers.co.kr/learn/courses/30/lessons/42579#

"""
장르 별로 가장 많이 재생된 노래 두 개를 모아라
노래는 고유번호로 구분 -> key
수록 순서
    1. 가장 많이 재생된 장르
    2. 장르 내에서 가장 많이 재생된 노래
    3. 고유번호가 낮은 노래(오름차순)
"""


def solution(genres, plays):
    """
    1. 장르랑 플레이 배열 순회하면서 딕셔너리 만든다. (k, v = 장르, (총 플레이 횟수, 노래 고유번호 배열)
    2. 그 딕셔너리에서 (플레이횟수)로 오름차순 정렬한다.
    3. 딕셔너리에서 해당 장르의 노래 고유번호 배열 중 0~1번 인덱스까지를 slicing해서 answer에 추가
    """
    dic = {}
    n = len(genres)

    # 장르 : 플레이 횟수, 노래 배열을 담은 딕셔너리 생성
    for i in range(n):  # O(N)
        genre = genres[i]
        play = plays[i]
        if genre not in dic:
            dic[genre] = [play, [(i, plays[i])]]
        else:
            p, songs = dic[genre]
            p += play
            songs.append((i, plays[i]))
            dic[genre] = [p, songs]
    # print(dic)

    sorted_dic = sorted(dic.items(), key=lambda x: (-x[1][0]))  # O(MlogM)
    answer = []

    # print(sorted_dic)

    for _, (_, songs) in sorted_dic:  # [(1, 600), (4, 2500)] # O(M)
        if len(songs) == 1:
            answer.append(songs[0][0])
            continue
        songs.sort(key=lambda x: (-x[1], x[0]))
        # print(songs)

        for i in range(2):
            answer.append(songs[i][0])

    return answer
