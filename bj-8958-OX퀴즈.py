개수 = int(input())
for i in range(개수):
    케이스 = input()
    점수 = 0
    점수리스트 = []
    for j in 케이스:
        if j == "O":
            점수 += 1
            점수리스트.append(점수)
        else:
            점수 = 0
    print(sum(점수리스트))


