def solution(clothes):
    clothes_dict = {}

    # 각 카테고리에 몇 가지 옷이 있는지 카운트한 딕셔너리
    for item in clothes:
        if item[-1] in clothes_dict.keys():
            clothes_dict[item[-1]] += 1
        else:
            clothes_dict[item[-1]] = 1

    count = 1
    for value in clothes_dict.values():  # 옷가지 갯수에 대해서
        count *= (value + 1)            # + 1은 해당 카테고리의 어떠한 옷도 입지 않는 경우

    return count - 1        # -1은 아무런 옷도 입지 않은 경우의 수를 제외하기 위함


clothes = [["yellow_hat", "headgear"], [
    "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))


"""
#1 
1. dict에 모두 담기 (빠르게 검색하기 위해)
2. 의상 조합 산출하기 (2개~의상종류갯수)
    1) 각각의 의상 조합에 대해 경우의 수 계산 --> 시간 복잡도 상승 
        (1) 의상 종류를 dict에서 검색
        (2) 몇 개 있는지 확인 후 저장
        (3) 모두 곱한 후 count 업데이트

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
