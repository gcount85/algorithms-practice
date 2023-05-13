import sys

x = str(sys.stdin.readline())

if int(x) < 99:
    print(x)
else: 
    숫자들 = [i for i in range(int(x)+1) if i > 110]
    count = 99
    for n in 숫자들:
        자리수 = list(map(int, str(n)))
        dif = []
        for i, v in enumerate(자리수):
            if i == (len(자리수)-1):
                break
            else:
                dif1 = v - 자리수[i+1]
                if (dif == []):
                    dif.append(dif1)
                else:
                    if dif1 == dif[0]:
                        dif.append(dif1)
        if (len(dif) == len(자리수)-1) and (len(set(dif)) == 1):
            count += 1
    print(count)
        

