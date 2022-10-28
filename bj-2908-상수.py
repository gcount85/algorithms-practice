
x, y = input().split()
X, Y = map(int, [x[::-1], y[::-1]])
print(max(X, Y))
