# https://www.acmicpc.net/problem/1110
# 0보다 크거나 같고, 99보다 작거나 같은 정수
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 
# 예시
# 26부터 시작한다. 
# 2+6 = 8이다. 
# 새로운 수는 68이다. 
# 6+8 = 14이다. 
# 새로운 수는 84이다. 
# 8+4 = 12이다. 
# 새로운 수는 42이다. 
# 4+2 = 6이다. 
# 새로운 수는 26이다.
# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.


import sys 

# 입력받기
N = sys.stdin.readline().strip()
# N = '1'
new_num = None
count = 0
sum = 0

while new_num != int(N):
    if count == 0:
        N1 = int(N[0])  
        N2 = int(N[-1]) 
        if int(N) < 10: 
            N1 = 0
            sum = N2   
        else:
            sum = N1 + N2
    else: 
        N1 = int(str(new_num)[0])
        N2 = int(str(new_num)[-1])
        if int(new_num) < 10:
            N1 = 0
            sum = N2
        else:
            sum = N1 + N2
    new_num = int(str(N2) + str(sum%10))
    count += 1

print(count)

# if N이 10보다 작은가?
    # 앞에 0을 붙인다
# else: 
    # 더한합 = 각 자리의 수를 더한다 
# 새로운수 = 주어진 수의 가장 오른쪽 자리 + 더한합의 오른쪽 자리 수 concat
# c += 1




