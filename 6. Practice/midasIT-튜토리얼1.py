from collections import deque


def solution(C: list):
    '''
    - 요약
        - 사용자가 방문한 URL 기록
        - 방문 기록을 근거로 사용자 현재 페이지 변경

    - 풀이
        - 두 가지 스택 사용하기
        - 'back' -> 방문 기록 스택에서 pop 해서 두 번째 스택에 push
        - 'next' -> 두 번째 스택에서 pop 해서 첫 번째 스택에 push
        - 'push' -> 방문 기록 스택에 해당 URL push + 두 번째 임시 스택 비우기
        - 현재 페이지: H의 top 요소
        - 중복 없는 이전 페이지 결과 반환: dict 구조를 이용해 중복 제거
    '''

    history_stack = deque()
    temp_stack = deque()

    for cmd, info in C:
        if (cmd == "PUSH"):
            url = info
            history_stack.append(url)
            temp_stack = deque()
        else:
            count = int(info)
            if (cmd == "BACK"):
                while (len(history_stack) != 0 and count != 0):
                    temp_stack.append(history_stack.pop())
                    count -= 1
            else:
                while (len(temp_stack) != 0 and count != 0):
                    history_stack.append(temp_stack.pop())
                    count -= 1

    answer = {}
    for i, v in enumerate(history_stack):
        answer[v] = i

    return list(answer.keys())
