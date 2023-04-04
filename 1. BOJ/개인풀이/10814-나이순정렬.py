import sys

input = sys.stdin.readline

N = int(input())
member = [input().split() + [i] for i in range(N)]
member.sort(key=lambda x: (int(x[0]), x[2]))

answer = []
for m in member:
    answer.extend([m[0], m[1]])
print((" ").join(answer))  # 여러 번 출력하는 것 보다 이게 더 빠르다
