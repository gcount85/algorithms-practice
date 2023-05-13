import sys

input = sys.stdin.readline

M = int(input())
sample_set = set()
for _ in range(M):
    if len(cmd := input().split()) == 2:
        x = int(cmd[1])
    cmd = cmd[0]
    if cmd == 'add':
        sample_set.add(x)
    elif cmd == 'remove':
        sample_set.discard(x)
    elif cmd == 'check':
        print(int(sample_set.__contains__(x)))
    elif cmd == 'toggle':
        if sample_set.__contains__(x):
            sample_set.discard(x)
        else:
            sample_set.add(x)
    elif cmd == 'all':
        sample_set = {i for i in range(1, 21)}
    else:
        sample_set.clear()
