'''
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 
사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 
게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. 
X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.
'''

import sys
from collections import deque, Counter

보드크기N = int(sys.stdin.readline())
사과갯수K = int(sys.stdin.readline())
사과좌표 = [tuple(map(int, sys.stdin.readline().split())) for _ in range(사과갯수K)]  #(3, 4), (2,5), (5,3)
방향전환수L = int(sys.stdin.readline())
방향전환정보 = [tuple(sys.stdin.readline().split()) for _ in range(방향전환수L)]  #[('3', 'D'), ('15', 'L'), ('17', 'D')]

def 뱀(보드크기N, 사과좌표, 방향전환정보):

    position_que = deque()
    position_que.append((1, 1))

    seconds = 0
    방향 = 'R'  #방향은 R, L, U, D 상하좌우 

    for i in 방향전환정보:    
        pop_cnt = 0
        전환초 = int(i[0])
        while pop_cnt != (전환초-seconds):  #전환초-SECONDS 뺀거
            현재좌표 = position_que[-1] #(1, 1)  #-1로 해야함 
            # 다음 좌표를 결정지음 
            if 방향 == 'R':
                다음좌표 = (현재좌표[0], 현재좌표[1]+1)
            if 방향 == 'L':
                다음좌표 = (현재좌표[0], 현재좌표[1]-1)
            if 방향 == 'U':
                다음좌표 = (현재좌표[0]-1, 현재좌표[1])
            if 방향 == 'D':
                다음좌표 = (현재좌표[0]+1, 현재좌표[1])
            # 사과 먹었는지 확인 
            if 다음좌표 in 사과좌표:
                position_que.append(다음좌표)
                사과좌표.remove(다음좌표)
            else:  # 사과 안 먹음 
                position_que.append(다음좌표)
                position_que.popleft()
            # 죽는 경우
            pop_cnt += 1
            갯수 = Counter(position_que)[position_que[-1]]  #-1이 되야함 
            if (방향 == 'R') and ((position_que[0][1] == 보드크기N) or (갯수 > 1)):
                seconds += pop_cnt
                return seconds
            elif (방향 == 'L') and ((position_que[0][1] == 1) or (갯수 > 1)):
                seconds += pop_cnt
                return seconds
            elif (방향 == 'U') and ((position_que[0][0] == 1) or (갯수 > 1)):
                seconds += pop_cnt
                return seconds
            elif (방향 == 'D') and ((position_que[0][0] == 보드크기N) or (갯수 > 1)):
                seconds += pop_cnt
                return seconds
            print(position_que)

        전환방향 = i[1]  # D, L
        if 방향 == 'R':
            if 전환방향 == "D":
                방향 = 'D'
            if 전환방향 == "L":
                방향 = 'U'
        elif 방향 == 'L':
            if 전환방향 == "D":
                방향 = 'U'
            if 전환방향 == "L":
                방향 = 'D'
        elif 방향 == 'U':
            if 전환방향 == "D":
                방향 = 'R'
            if 전환방향 == "L":
                방향 = 'L'
        elif 방향 == 'D':
            if 전환방향 == "D":
                방향 = 'L'
            if 전환방향 == "L":
                방향 = 'R'
        seconds += pop_cnt
    return seconds
            
print(뱀(보드크기N, 사과좌표, 방향전환정보))

        



'''슈도코드
(1,1)을 넣은 큐
열을 하나씩 증가시키며 큐에 넣고, 기존 것을 팝하며 카운트 계산
    if 큐에 넣었는데 사과자리다 -> pop X
    if 벽자리다 -> 다음 방향전환 초수와 비교하여 죽었으면 result 반환 
    if 큐에 넣었는데 이미 있다 -> 주금 result 반환
방향전환 초수에 다다르면 방향에 따라 행을 증가시키거나 열을 증가시킴


'''

