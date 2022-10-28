import sys

def 골드바흐():
    # 개수 = int(sys.stdin.readline())

    for c in range(int(sys.stdin.readline())):
        숫자 = int(sys.stdin.readline())
        소수 = []
        for i in range(2,숫자):
            약수개수 = len([n for n in range(2,숫자) if i != n and i % n == 0])
            if 약수개수 == 0:
                소수.append(i)
        파티션 = []
        for i1, a in enumerate(소수):
            for i2, b in enumerate(소수):
                temp = sorted([a, b])
                차이 = (abs(a-b), temp)
                if i2 >= i1 and a+b == 숫자:  
                    if 차이[0] == 0:
                        print(파티션[0][1][0], 파티션[0][1][1])
                        break
                    elif 차이 not in 파티션:
                        파티션.append(차이)

        # 파티션 = [(abs(a-b), temp) for a in 소수 for b in 소수 if a+b == 숫자 and (temp := sorted([a, b]) not in 파티션)]
        파티션.sort()
        # print(파티션)
        print(파티션[0][1][0], 파티션[0][1][1])

골드바흐()

# print(소수)
# for A, B in zip(소수, 소수):
#     if A+B == 숫자:
#         print(f"{A} {B}")

# 파티션 구하는 부분
# for a in 소수:
#     for b in 소수:
#         if a+b == 숫자:
#             파티션.append((abs(a-b), temp := sorted([a, b])))

# 주어진 숫자보다 작은 소수를 찾기  
# 소수리스트 두개를 만듦(서로 복사?)
# 자기끼리 먼저 더해봄 
# 발견하면 리턴
# for 문을 돌리면서 더함 
# 차이가 가장 적은 거 출력 

