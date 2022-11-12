# https://www.acmicpc.net/problem/1991

import sys


# 전위순회
pre = ""
def preorder(key: str):
    global pre
    node = tree_dict[key] # {A: (B, C)} 노드는 (b, c)
    pre += key # 노드 방문
    if node[0] != None:
        preorder(node[0]) # 왼쪽 서브 트리 순회
    if node[1] != None:
        preorder(node[1]) # 오른쪽 서브 트리 순회

# 중위 순회
ino = ""
def inorder(key: str):
    global ino
    node = tree_dict[key] # {A: (B, C)} 노드는 (b, c)
    if node[0] != None:
        inorder(node[0]) # 왼쪽 서브 트리 순회
    ino += key
    if node[1] != None:
        inorder(node[1]) # 오른쪽 서브 트리 순회

# 후위 순회
post = ""
def postorder(key: str):
    global post
    node = tree_dict[key] # {A: (B, C)} 노드는 (b, c)
    if node[0] != None:
        postorder(node[0]) # 왼쪽 서브 트리 순회
    if node[1] != None:
        postorder(node[1]) # 오른쪽 서브 트리 순회
    post += key

N = int(sys.stdin.readline())
tree_dict = dict()
for i in range(N):
    node = sys.stdin.readline().split()  # [A, B, C]
    key = node[0]
    # left, right 노드가 점인지 아닌지 확인하기 
    if node[1] != '.':
        left = node[1]
    else:
        left = None
    if node[2] != '.':
        right = node[2]
    else:
        right = None
    tree_dict[key] = (left, right)  # 딕셔너리에 key에 알파벳, value에 왼쪽, 오른쪽 노드 추가

# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력
preorder('A')
print("")
inorder('A')
print("")
postorder('A')

print(f"{pre}\n{ino}\n{post}")


