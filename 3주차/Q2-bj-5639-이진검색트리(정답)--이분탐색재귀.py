import sys
sys.setrecursionlimit(10**6)

nodes = []
while True:                            
    try:
        nodes.append(int(sys.stdin.readline()))
    except:
        break
    

# 이분 탐색 알고리즘... (트리를 더 작은 트리로 계속 나눔)
def postorder(start, end):
    if start > end:
        return
    mid = end + 1                         # 오른쪽 노드가 없을 경우

    for i in range(start+1, end+1):
        if nodes[start] < nodes[i]:
            mid = i
            break

    postorder(start+1, mid-1)               # 왼쪽 확인
    postorder(mid, end)                   # 오른쪽 확인
    print(nodes[start])

postorder(0, len(nodes)-1)