
개수 = int(input())
for i in range(개수):
    케이스 = list(map(int, input().split(" ")))
    # 케이스 = [테스트케이스개수, 점수1, 점수2, 점수3 ... ]
    평균 = (sum(케이스) - 케이스[0]) / 케이스[0]
    c = 0
    for index, j in enumerate(케이스):
        if index > 0 and j > float(평균):
            c += 1
    print(f"{c/케이스[0]*100:.3f}%")






