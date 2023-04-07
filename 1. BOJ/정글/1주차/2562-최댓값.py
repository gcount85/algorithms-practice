리스트 = []
for i in range(9):
    자연수 = int(input())
    리스트.append(자연수)

최댓값 = max(리스트) 
print(최댓값)
print(리스트.index(최댓값)+1)

