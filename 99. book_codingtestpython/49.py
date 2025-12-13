# https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3
# 39분 solved


def is_valid(now_hp, require, selected_dungeons, new_i):
    if now_hp < require:
        return False
    if new_i in selected_dungeons:
        return False
    return True


def find_solution(now_hp, dungeons, selected_dungeons, answer):
    answer[0] = max(len(selected_dungeons), answer[0])
    for new_i, (require, consume) in enumerate(dungeons):
        # 그 던전을 탐험할 수 있으면 진행
        if is_valid(now_hp, require, selected_dungeons, new_i):
            selected_dungeons.add(new_i)
            new_hp = now_hp - consume
            find_solution(new_hp, dungeons, selected_dungeons, answer)
            selected_dungeons.remove(new_i)


def solution(hp, dungeons):
    """
    1. for start in every dungeons:
        1-1. start 부터 던전 탐험 시작
            1-1-1. isValid 하면:
                1) 선택 던전에 현재 던전 추가, 피로도 빼기
                2) 재귀 탐색 (지금까지 탐험한 던전, 현재 피로도)
                3) 재귀 탐색 false 뜨면:
                    지금까지 던전 set에서 현재 던전 제거
                    피로도 원상복구
                4) 던전 탐험 개수 최댓값 갱신
            1-1-2. valid 안하면 return False
    """
    answer = [-1]
    find_solution(hp, dungeons, set(), answer)
    return answer[0]
