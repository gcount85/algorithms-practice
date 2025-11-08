def solution(string_list, query_list):
    dic = {}
    answer = []
    for s in string_list:
        dic[s] = 1
    for q in query_list:
        if dic.get(q, 0) == 1:
            answer.append(True)
        else:
            answer.append(False)
    return answer


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(
    solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"])
)  # 반환값 : [True, False, False, True]
