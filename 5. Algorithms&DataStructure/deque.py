# 백준 10866번 참고

import sys


class Deque():

    def __init__(self):
        self.deque = []

    def empty(self):
        return int(len(self.deque) == 0)

    def size(self):
        return len(self.deque)

    def front(self):
        if (self.deque == []):
            return -1
        return self.deque[0]

    def back(self):
        if (self.deque == []):
            return -1
        return self.deque[-1]

    def push_front(self, X):
        self.deque.insert(0, X)

    def push_back(self, X):
        self.deque.append(X)

    def pop_front(self):
        if (self.deque == []):
            return -1
        return self.deque.pop(0)

    def pop_back(self):
        if (self.empty() == 1):
            return -1
        return self.deque.pop()


any_deque = Deque()

N = int(sys.stdin.readline())

for _ in range(N):
    cmd = sys.stdin.readline().strip().split(" ")
    # print(cmd)
    if len(cmd) == 2:
        result = eval(f"any_deque.{cmd[0]}({cmd[1]})")
    else:
        result = eval(f"any_deque.{cmd[0]}()")
    if result != None:
        print(result)
