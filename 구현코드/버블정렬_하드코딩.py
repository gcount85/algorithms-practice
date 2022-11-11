import sys

횟수 = int(sys.stdin.readline())
숫자들 = [int(sys.stdin.readline()) for _ in range(횟수)]


bool = True
while bool == True:
    s = 0
    for i, v in enumerate(숫자들):
        if i == len(숫자들)-1:
            break
        if v > 숫자들[i+1]:    
            숫자들[i], 숫자들[i+1] = 숫자들[i+1], 숫자들[i]   
            s += 1
    if s == 0:
        bool = False

for i in 숫자들:
    print(i)


    
