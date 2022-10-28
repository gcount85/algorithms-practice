개수 = int(input())
for i in range(개수):
    출력 = ""
    반복횟수, 문자열 = input().split(" ")   
    for j in 문자열:
        출력 += j*int(반복횟수)
    print(출력)