# 정수 배열을 오름차순 정렬해서 반환하는 solution() 함수 완성
# 정수 배열 길이는 2 이상 10^5 (10만) 이하
# 정수 배열의 각 데이터 값은 -100,000 이상 100,000 이하


def solution(list):
    list.sort()
    return list


# TEST 코드 입니다.
print(solution([1, -5, 2, 4, 3]))  # 반환값 : [-5, 1, 2, 3, 4]
print(solution([2, 1, 1, 3, 2, 5, 4]))  # 반환값 : [1, 1, 2, 2, 3, 4, 5]
print(solution([1, 6, 7]))  # 반환값 : [1, 6, 7]
