import sys
x = str(sys.stdin.readline())
if int(x) < 99:
    print(x)
else: 
    숫자들 = [i for i in range(int(x)+1) if i > 110]
    count = 99
    for n in 숫자들:
        자리수 = list(map(int, str(n)))
        print(자리수)
        for i, v in enumerate(자리수):
            if i == len(자리수)-1:
                break
            else:
                dif = v - v[i+1]
        count += 1
    print(count)
        

