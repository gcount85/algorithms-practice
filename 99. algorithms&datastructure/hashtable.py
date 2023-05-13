"""
저장할 키와 밸류

키: "apple", 값: 5
키: "banana", 값: 7
키: "orange", 값: 9

"""


def hash_function(key):
    # 해당 문자의 아스키코드 값을 모두 더하는 해쉬 함수를 만들었다
    ord_sum = 0
    for char in key:
        ord_sum += ord(char)
    return ord_sum


# 해쉬코드를 생성한다
apple_hash = hash_function("apple")
banana_hash = hash_function("banana")
orange_hash = hash_function("orange")

print(apple_hash, banana_hash, orange_hash)  # 530 609 636

# 배열을 만들고 배열 사이즈(10) 범위 안에 인덱스가 위치하도록 해쉬 코드를 배열 사이즈로 나눈 나머지를 취한다
hash_table_array = [None] * 10
apple_index = apple_hash % 10
banana_index = banana_hash % 10
orange_index = orange_hash % 10

# 그렇게 추출한 인덱스로 배열에 value를 할당한다
hash_table_array[apple_index] = 5
hash_table_array[banana_index] = 7
hash_table_array[orange_index] = 9

print(hash_table_array)  # [5, None, None, None, None, None, 9, None, None, 7]
