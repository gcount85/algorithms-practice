def solution(arr, target):
    """
    1. arr를 정렬함
    2. 딕셔너리를 만들음
    3. arr를 순회하면서, 배열[i]에 값 유무 표기
    4. arr 다시 순회하면서, 배열[target - arr]이 1이면 return true
        없으면 retur False

    """

    lst = {}
    for e in arr:  # O(N)
        lst[e] = 1
    for e in arr:  # O(N)
        if target - e == e:
            continue
        if lst.get(target - e, 0) == 1:
            return True
    return False


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution([1, 2, 888888888888888888888, 4, 8], 6))  # 반환값 : True
print(solution([2, 3, 5, 9], 10))  # 반환값 : False
