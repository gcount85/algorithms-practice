def is_splited(large_sum, A, K):
    block_sum = 0
    block_count = 0

    for a in A:
        if (block_sum + a > large_sum): # a를 더한 값과 비교해야 건너뛰는 값이 없음
            block_sum = a               # sum을 구할 원소 기준 재설정
            block_count += 1
            if block_count == K:        # K개로 쪼개려면 block_count는 K 미만이여야 함
                return 0
        else:
            block_sum += a

    return 1


def search(low, high, A, K, answer):
    if low > high:
        return answer
    else:
        mid = (low + high) // 2
        if (is_splited(mid, A, K) == 1):
            answer = min(mid, answer)
            return search(low, mid-1, A, K, answer)
        else:
            return search(mid+1, high, A, K, answer)



def solution(K, M, A):
    N = len(A)
    answer = M * N
    high = sum(A)
    low = max(A) # low를 0으로 잡아야 엣지 케이스 통과

    if K == 1:
        return high
    if K >= N:
        return low
    if high == low:
        return low
    
    answer = search(low, high, A, K, answer)
    return answer


K = 3
M = 99
A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(solution(K, M, A))


'''
- 엣지케이스: 
    1. 모두 0인 배열 A. V
    2. K가 배열의 길이와 같거나 크다면 V !!!! 
    3. K가 1이라면 V
    4. block의 length가 0일 수도 있음 !!!! 
    5. 다 더한 값이 M과 같다면 ?
    6. M보다 크지 않다는 말이, 최대값이 곧 M이라는 뜻은 아님!!!

- 배열 쪼개기 확인 함수
1. 배열을 주어진 sum 값을 최대 sum 값으로 유지하면서 K개로 쪼갤 수 있는지 확인

- 이분탐색 함수
1. 0부터 최대 합까지 범위 지정
2. mid 값을 최대 합으로 리스트를 쪼갤 수 있는가:
    1) 가능하면 -> answer에 할당 + 배열의 왼쪽 탐색
    2) 불가능하면 배열의 오른쪽 탐색

- 0 ~ largest sum 
1) 블럭 길이로 자르기 (0~N)
2) large sum 기준으로 자르기 (0~15)
3) M을 찾아서 M 앞뒤로 자르기??? 

- 문제요약: 
배열 A를 K개의 블럭으로 나눔 
    반드시 1개 이상의 블럭
    블럭의 길이는 0일 수도 있음
배열 A의 원소는 M이하 
블락 총합의 최댓값이 가장 작은 것 

- 리턴:
    the minimal large sum 

'''
