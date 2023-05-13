def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# 함수 테이블 생성
function_table = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

# 함수 테이블 사용 예시
result = function_table['add'](3, 4)
print(result)  # 출력: 7

result = function_table['subtract'](3, 4)
print(result)  # 출력: -1

result = function_table['multiply'](3, 4)
print(result)  # 출력: 12

result = function_table['divide'](12, 4)
print(result)  # 출력: 3.0

# 동적으로 함수 포인터를 이용하여 함수 호출하기
func_name = input("add, substract, multiply, divde 중 하나 입력: ")
param1, param2 = map(int, input("숫자 두 개 입력: ").split(" "))
print(function_table[func_name.strip()](param1, param2))
