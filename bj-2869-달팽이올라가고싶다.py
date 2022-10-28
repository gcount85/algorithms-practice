import sys
import math
A, B, V = map(int, sys.stdin.readline().split())
# 정상에 도달하면 멈춘다는 뜻은, 계산을 멈추는 기준을 V에서 B만큼 뺀 값으로 잡아야 함 ... 
print(math.ceil((V-B)/(A-B)))

