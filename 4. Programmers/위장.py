from itertools import combinations


def solution(clothes):
    clothes_dict = {}
    count = 0

    # 여기서 아예 옷 가지의 수만 카운트해서 딕셔너리 만들기 
    for item in clothes:
        if item[-1] in clothes_dict.keys():
            clothes_dict[item[-1]] += 1
        else:
            clothes_dict[item[-1]] = 1
    
    clothes_count = sum(clothes_dict.values())

    for i in range(2, clothes_count + 1):
        comb = list(combinations(clothes_dict.keys(), i))
        # print(comb)
        temp = 1
        for c in comb:  # tuple
            for k in c:
                temp *= clothes_dict[k]
            count += temp
            temp = 1

    count += clothes_count
    return count


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))


"""
#1 
1. dict에 모두 담기 (빠르게 검색하기 위해)
2. 의상 조합 산출하기 (2개~의상종류갯수)
    1) 각각의 의상 조합에 대해 경우의 수 계산 --> 시간 복잡도 상승 
        (1) 의상 종류를 dict에서 검색
        (2) 몇 개 있는지 확인 후 저장
        (3) 모두 곱한 후 count 업데이트

#2 
1. 각각의 의상 종류마다 몇 개의 옷이 있는지 알려주는 딕셔너리 생성
2. 경우의 수 계산
    1) 의상 종류를 dict에서 검색
    2) 몇 개 있는지 확인 후 저장
    3) 모두 곱한 후 count 업데이트

- 조합 원소 길이: 1개 ~ 의상의 종류 갯수
- 어떤 종류의 의상을 입을 것인지 경우의 수를 다 구해서 각자 더함 
    - 1개만 입으면 총 의상 갯수가 경우의 수 
    - 2개 이상 입으면 같은 종류의 여러 개 의상 있는 애들 곱하기 해야 함 

- 문제 요약:
    - 매일 다른 옷을 입도록 조합
    - 조합의 수를 return
- 제한사항:
    - 의상의 이름, 의상의 종류로 구성
    - 의상의 수: 1개 이상 30개 이하
    - 중복 없음
    - 문자열의 길이: 1이상 20이하 
    - 문자열의 구성: 알파벳 소문자, "_"
    - 최소 하루 한개 이상은 입어야 함

- try
    - itertools의 combination 사용 + 옷의 개수를 세는 딕셔너리 또 만듦 => 시간복잡도 ↑

"""
