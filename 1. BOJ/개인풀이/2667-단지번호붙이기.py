from sys import stdin

n = int(stdin.readline())
town = [stdin.readline() for _ in range(n)]
visit = [[0] * n for _ in range(n)]


def dfs(n, i, j, num):
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = i + dx, j + dy
        if not (0 <= nx < n and 0 <= ny < n):
            continue
        if town[nx][ny] == '0' or visit[nx][ny] == 1:
            continue
        visit[nx][ny] = 1
        num = dfs(n, nx, ny, num + 1)
    return num

ans = []
cnt = 0
for i in range(n):
    for j in range(n):
        if town[i][j] == '0' or visit[i][j] == 1:
            continue
        visit[i][j] = 1
        cnt += 1
        num = 1
        ans.append(dfs(n, i, j, num))


ans.sort()
print(cnt, *ans)

'''
1. 0부터 n까지 이중 반복문으로 dfs 
    1) dfs_visit으로 노드 카운팅 
2. dfs 방문이 이루어질 때마다 카운팅 + 노드 개수 저장
3. 카운팅, 노드 개수를 오름차순으로 출력  

'''