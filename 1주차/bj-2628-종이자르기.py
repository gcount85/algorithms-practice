import sys

width, height = map(int, sys.stdin.readline().split())   
(line_num := [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]).sort()

h_point = [i[1] for i in line_num if i[0] == 0]  
temp1 = []
if len(h_point) == 0:
    temp1.append(height)        
else:
    for i, v in enumerate(h_point):
        if i == 0:
            temp1.append(v-0)        
        if i == len(h_point)-1:
            temp1.append(height-v)
        else:
            temp1.append(h_point[i+1]-v)

w_point = [i[1] for i in line_num if i[0] == 1]  
temp2 = []
if len(w_point) == 0:
    temp2.append(width)        
for i, v in enumerate(w_point):
    if i == 0:
        temp2.append(v-0)        
    if i == len(w_point)-1:
        temp2.append(width-v)
    else:
        temp2.append(w_point[i+1]-v)

print(max(temp1)*max(temp2))


