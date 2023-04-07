
자연수리스트 = []
for i in range(3):
    자연수 = input()
    자연수리스트.append(자연수)
곱한값 = eval("*".join([str(n) for n in 자연수리스트]))

# 17037300 
for n in range(10):  # 1~ 9 
    c = 0
    for i in str(곱한값):
        if i == str(n):
            c += 1
    print(c)



    # 0의 개수
    # 1의 개수 ...

