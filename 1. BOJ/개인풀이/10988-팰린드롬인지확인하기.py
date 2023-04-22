
string = input().strip()

n = len(string)
s, e = 0, n-1


def solution(n, s, e):
    for _ in range(n//2):
        if string[s] == string[e]:
            s += 1
            e -= 1
        else:
            print(0)
            return
    print(1)


solution(n, s, e)
