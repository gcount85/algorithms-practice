import sys
import heapq

class DoubleEndedPriorityQueue:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.entry_map = {}

    def add(self, value):
        if value in self.entry_map:
            self.entry_map[value] += 1
        else:
            min_entry = [value, value]
            max_entry = [-value, value]

            heapq.heappush(self.min_heap, min_entry)
            heapq.heappush(self.max_heap, max_entry)

            self.entry_map[value] = 1

    def remove_min(self):
        try:
            while self.min_heap:
                value = heapq.heappop(self.min_heap)[1]
                if value in self.entry_map:
                    self.entry_map[value] -= 1
                    if self.entry_map[value] == 0:
                        del self.entry_map[value]
                    return value
        except KeyError:
            return

    def remove_max(self):
        try:
            while self.max_heap:
                value = heapq.heappop(self.max_heap)[1]
                if value in self.entry_map:
                    self.entry_map[value] -= 1
                    if self.entry_map[value] == 0:
                        del self.entry_map[value]
                    return value
        except KeyError:
            return

    def is_empty(self):
        return len(self.entry_map) == 0

t = int(sys.stdin.readline())

for _ in range(t):

    k = int(sys.stdin.readline())  # k <= 1000000
    dq = DoubleEndedPriorityQueue()

    for _ in range(k):
        cmd, num = sys.stdin.readline().strip().split()
        if cmd == 'D':
            if num == '-1': # 최솟값 삭제 
                dq.remove_min()
            else: # 최대값 삭제
                dq.remove_max()
        elif cmd == 'I':
            dq.add(int(num))
            
    if dq.is_empty():
        print('EMPTY')
    else:
        print(dq.remove_max(), dq.remove_min())


