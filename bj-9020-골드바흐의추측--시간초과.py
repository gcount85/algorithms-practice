import sys, math

for c in range(int(sys.stdin.readline())):
    숫자 = int(sys.stdin.readline())
    소수 = []
    for i in range(2,숫자):  
        약수개수 = len([n for n in range(2,int(math.sqrt(i))+1) if i != n and i % n == 0])
        if 약수개수 == 0:
            소수.append(i)
    (파티션 := [(abs(a-b), [a, b]) for i1, a in enumerate(소수) for i2, b in enumerate(소수) if i2 >= i1 and a+b == 숫자]).sort()
    print(파티션[0][1][0], 파티션[0][1][1])

# 주어진 숫자보다 작은 소수를 찾기  
# 소수리스트 두개를 만듦
# 자기끼리 먼저 더해봄 
# 발견하면 리턴
# for 문을 돌리면서 더함 
# 차이가 가장 적은 거 출력 

