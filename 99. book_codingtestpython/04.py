"""
https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3
시험은 최대 10000 문제 (-> NlogN 이하로?)
return 시 오름차순
1번 수포자: 12345 반복
2번 수포자: 21 23 24 25 21 23 24 25 반복.. 22만 빼고 반복
    홀수 문제는 2번, 짝수 문제는 반복
3번 수포자: 33 11 22 44 55 반복

1. [반복문] 각각의 답을 정답 배열 원소랑 바로 비교 & 점수 누적 계산 -> O(N)으로 조회
2. 최고 정답자만 배열에 남기고, 복수면 오름차순 정렬 -> O(NlogN)
"""


def solution(answers):
    length = len(answers)
    first = [1, 2, 3, 4, 5]  # length = 5
    second = [2, 1, 2, 3, 2, 4, 2, 5]  # len = 8
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # len = 10
    scores = [0] * 3

    for i in range(length):  # O(3N)
        ans = answers[i]
        ansNum = i + 1
        sub = [0, 0, 0]

        firstDetermine = ansNum % 5
        if firstDetermine == 0:
            sub[0] = first[-1]
        else:
            sub[0] = first[firstDetermine - 1]

        secondDetermine = ansNum % 8
        if secondDetermine == 0:
            sub[1] = second[-1]
        else:
            sub[1] = second[secondDetermine - 1]

        thirdDetermine = ansNum % 10
        if thirdDetermine == 0:
            sub[2] = third[-1]
        else:
            sub[2] = third[thirdDetermine - 1]

        for number, a in enumerate(sub):
            if a == ans:
                scores[number] += 1

    maxScore = max(scores)
    # print(f"scores: {scores}")
    answer = []
    for i, a in enumerate(scores):
        if a == maxScore:
            answer.append(i + 1)
    return answer
