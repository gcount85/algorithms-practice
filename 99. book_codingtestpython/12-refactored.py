def solution(prices):
    """
    - 스택 초기화
    - [반복] prices 길이만큼 n번 반복
        - 인덱스로 원소를 검사한다
        - prices[스택 top] 원소랑 prices[i] 원소 값을 비교한다
        - 후자가 전자보다 "작으면", 후자가 전자보다 같거나 클 때까지 다음을 반복한다:
            - answer[스택top]의 값은 (i - 스택 top)이다.
            - 스택 pop
        - i를 push한다
    - 스택에 원소가 남아 있으면:
        - [반복] 원소가 없을 때까지:
            - answer[스택top] = 마지막 인덱스 - 스택 top
            - 스택 pop
    """

    n = len(prices)
    answer = [0] * n
    stack = [0]

    for i in range(n):
        candid = prices[i]
        topIndex = stack[-1]
        topPrice = prices[topIndex]
        isDropped = topPrice > candid
        while isDropped:
            topIndex = stack.pop()
            answer[topIndex] = i - topIndex
            if stack:
                newTopPrice = prices[stack[-1]]
                isDropped = newTopPrice > candid
            else:
                break
        stack.append(i)

    while stack:
        popped = stack.pop()
        answer[popped] = n - 1 - popped

    return answer
