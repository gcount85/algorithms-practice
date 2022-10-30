import sys, random

#키는 100이하,  오름차순 출력 
키 = [int(sys.stdin.readline()) for _ in range(9)]
더한값 = 0
while 더한값 != 100:
    샘플 = random.sample(키, 7)
    더한값 = sum(샘플)
for i in sorted(샘플):
    print(i)


