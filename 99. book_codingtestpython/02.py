"""
배열 중복값 제거
내림차순 정렬
배열 길이는 2 ~ 100,000(10만, 10^5)
제한시간 3초라고 가정
=> 배열 길이가 10만 개니까, N^2 이상 시간복잡도는 안 됨!

"""


def solution(input):
    no_dups_list = list(set(input))  # O(N) + O(N)
    no_dups_list.sort(reverse=True)  # O(NlogN)
    return no_dups_list


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution([4, 2, 2, 1, 3, 4]))  # 반환값 : [4, 3, 2, 1]
print(solution([2, 1, 1, 3, 2, 5, 4]))  # 반환값 : [5, 4, 3, 2, 1]
