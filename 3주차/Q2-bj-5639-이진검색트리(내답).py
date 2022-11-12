import sys

nodes = []
while True:                            
    try:
        nodes.append(int(sys.stdin.readline()))
    except:
        break
    
# 루트 노드 만들기 
root = nodes[0]
root_lefts = []
root_lefts_right = []
root_rights = []
root_rights_right = []

for i, v in enumerate(nodes):
    if i > 0 and v < root:
        root_lefts.append(v)
    elif i > 0 and v > root:
        root_rights.append(v)

for idx, val in enumerate(root_lefts):
    if idx > 0 and val > root_lefts[idx-1]:
        root_lefts_right.extend(root_lefts[idx:])
        break

for j, k in enumerate(root_rights):
    if j > 0 and k > root_rights[j-1]:
        root_rights_right.extend(root_rights[j:])
        break

idx0 = root_lefts.index(root_lefts_right[0])  # 3
idx1 = root_rights.index(root_rights_right[0])  # 2

for A, B in zip(root_lefts[idx0-1::-1], root_lefts_right):
    print(A)
    print(B)
for A, B in zip(root_rights[idx1-1::-1], root_rights_right):
    print(A)
    print(B)
print(root)


# print(root)
# print(root_lefts)
# print(root_lefts_right)
# print(root_rights)
# print(root_rights_right)

# print(root_lefts[idx0-1::-1])

# while True:
#     for A, B in root_lefts, root_rights:
#         if A != B:
#             print



