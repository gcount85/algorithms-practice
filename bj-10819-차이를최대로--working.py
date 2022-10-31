import sys, random

def 더해(i, ans):
    if i == 0:
        return 0
    else:
        return 더해(i-1, ans) + abs(ans[i-1]-ans[i])

# N = int(sys.stdin.readline()) # 3 <= N <= 8   
N = 6   
A = [20, 1, 15, 8, 4, 10]
# lst = list(map(int, sys.stdin.readline().split()))
lst = A
ans = []
합 = 0
for i in range(N):
    if len(lst) > 1:
        최소값 = min(lst)
        최대값 = max(lst)
        lst.remove(최소값)
        lst.remove(최대값)
        ans.append(최소값)
        ans.append(최대값)
    elif len(lst) == 1:
        ans.append(lst[0])
    elif len(lst) == 0:
        break
print(더해(N-1, ans))


    
        




