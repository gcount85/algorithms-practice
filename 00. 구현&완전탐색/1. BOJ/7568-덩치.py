import sys

input = sys.stdin.readline

N = int(input())
member = [tuple(map(int, input().split())) for _ in range(N)]
# print(member)

answer = []
for s, (weight, height) in enumerate(member):
    e = 0
    count = 0
    while (e < N):
        cmp_weight, cmp_height = member[e][0], member[e][1]
        if (e != s and cmp_height > height and cmp_weight > weight):
            count += 1
        e += 1
    answer.append(count+1)
print(*answer)

'''
x > p 그리고 y > q 일때, 덩치가 크다 
나의 덩치 등수: 나보다 더 큰 덩치를 가진 사람의 수 + 1
덩치 등수가 같은 사람이 존재할 수 있음 
2 ≤ N ≤ 50
10 ≤ x, y ≤ 200

'''
