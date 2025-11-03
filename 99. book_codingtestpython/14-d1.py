"""
- 행을 선택, 삭제, 복구 -> 스택
- 처음 표의 행 개수 n. 5~100만 => NLogN 이하
- 처음 선택 된 행의 위치 정수 k
- 명령어 문자열 배열 cmd. 1~20만

- 원본 1차원 배열이 있고, 인덱스를 요리조리 움직여서 명령어를 수행하자
    - 삭제하는 경우 값을 0으로 처리해보기
    - 단 이러면 U 3 같은 명령어 칠 때, 중간에 삭제되서 빈집 된 원소도 건너 뛰어야 함. -> 살아남은 인덱스만 남은 배열을 하나 더 만들자 or stack을 훑으면서 건너뛰어야 하는애들이 있으면 연산해서 더 건너뛰거나
    # 01234567
    # 0123-567
    - (마지막 행 삭제 예외 조심)
- 그리고 삭제된 원소는 스택에 보관했다가 복구했다가 함
- 마지막에 원본 배열에서 값이 0이 아닌 애들만 O로 표기하면 됨
"""


def solution(n, k, cmd):
    """
    1. 삭제된 애들 담을 stack, O로 채워진 n 길이의 배열 lst,
    2. k는 현재 index 위치다.
        - lst[k]
    2. [분기] 명령어를 해석한다.
        2-1. D X :
            - 스택 원소에 k이상 k+X이하 몇갠지 count 센다.
            - lst[k+X+count] 위치로 간다
            - while 그 위치가 빈집이라면:
                k ++1
        2-2. U X :
            - 스택 원소에 k-X이상 k이하 몇갠지 count 센다.
            - lst[k-X-count] 위치로 간다
            - while 그 위치가 빈집이라면:
                k --1
        2-3 C :
            - lst[k] = 'X'
            - stack에 k push
        2-4 Z :
            - lst[stack pop] = 'O'
    3. lst를 join
    """
    stack = []
    lst = ["O"] * n
    i = k
    for c in cmd:
        if c.startswith("D"):
            _, X = c.split(" ")
            X = int(X)
            count = len([i for i in stack if k <= i <= k + X])
            k = k + X + count
        elif c.startswith("U"):
            _, X = c.split(" ")
            X = int(X)
            count = len([i for i in stack if k - X <= i <= k])
            k = k - X - count
        elif c == "C":
            lst[k] = "X"
            stack.append(k)
        elif c == "Z":
            lst[stack.pop()] = "O"
        if k == n - 1:
            while k >= 0 and lst[k] == "X":
                k -= 1
        else:
            while k < n and lst[k] == "X":
                k += 1
        # print(''.join(lst))

    answer = "".join(lst)
    return answer
