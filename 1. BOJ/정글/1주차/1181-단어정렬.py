import sys

str = [(input := sys.stdin.readline().strip(), len(input)) for _ in range(int(sys.stdin.readline()))]
no중복 = list(set(str))
no중복.sort(key=lambda x: (x[1], x[0]))
for i in no중복:
    print(i[0])