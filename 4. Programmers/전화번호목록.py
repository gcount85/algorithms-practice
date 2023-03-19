def solution(phone_book):
    phone_dict = set(phone_book)
    for i in phone_dict:  # 백만 * 20
        for j in range(1, len(i)):
            if i[:j] in phone_dict:
                return False
    return True


"""
- 리턴:
    - 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false
    - 그렇지 않으면 true를 

- 제한사항:
    - 전화번호 중복없음
    - 전화번호 부의 길이는 1이상 백만 이하
    - 전화번호 길이는 1이상 20 이하



"""
