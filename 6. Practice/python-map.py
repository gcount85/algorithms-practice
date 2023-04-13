dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
s = (100, 100)

edges = list(map(lambda x: x + s, dir))
# [(-1, 0, 100, 100), (1, 0, 100, 100), (0, -1, 100, 100), (0, 1, 100, 100)]
print(edges)