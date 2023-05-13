# 상태 기반 CRDT : 변경된 상태를 전파하여 병합
class GSet:
    def __init__(self):
        self.set = set()

    def add(self, value):
        self.set.add(value)

    def query(self, value):
        return value in self.set

    def merge(self, other): 
        self.set |= other.set # 합집합 연산 

# 노드 A와 B 생성
A = GSet()
B = GSet()

# 노드 A에 1 추가
A.add(1)

# 노드 B에 2 추가
B.add(2)

# 노드 A와 B를 병합
A.merge(B)
B.merge(A)

print(A.set)  # 출력: {1, 2}
print(B.set)  # 출력: {1, 2}



# 작업 기반 CRDT : 변경 작업 자체를 다른 노드에게 전파 후 적용시킴
class AddOnlySet:
    def __init__(self):
        self.set = set()

    def apply_add(self, value):
        self.set.add(value)

    def query(self, value):
        return value in self.set

    def propagate_add(self, value, other): # 다른 노드에게 value 추가 작업을 전파함
        other.apply_add(value)

# 노드 C와 D 생성
C = AddOnlySet()
D = AddOnlySet()

# 노드 C에 1 추가
C.apply_add(1)

# 노드 D에 2 추가
D.apply_add(2)

# 노드 C와 D의 변경 작업 전파
C.propagate_add(1, D)
D.propagate_add(2, C)

print(C.set)  # 출력: {1, 2}
print(D.set)  # 출력: {1, 2}

