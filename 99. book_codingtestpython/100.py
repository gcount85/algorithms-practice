# https://school.programmers.co.kr/learn/courses/30/lessons/77484


def solution(lottos, win_nums):
    """
    1. 둘 다 정렬
    2. 0을 제외하고 일치하는 개수를 알아내고
    3. 0을 맞춘 번호로 쳐서
    4. 등수 계산
    """

    lottos.sort()
    win_nums.sort()
    my_p = 0
    win_p = 0
    zeros = len([i for i in lottos if i == 0])
    right = 0
    # print(lottos, win_nums)

    while my_p < 6 and win_p < 6:
        if lottos[my_p] == 0:
            my_p += 1
            continue
        if lottos[my_p] == win_nums[win_p]:
            right += 1
            my_p += 1
            win_p += 1
        elif lottos[my_p] > win_nums[win_p]:
            win_p += 1
        elif lottos[my_p] < win_nums[win_p]:
            my_p += 1

    # print(zeros, right)
    return [
        7 - (right + zeros) if 7 - (right + zeros) <= 5 else 6,
        7 - right if 7 - right <= 5 else 6,
    ]
