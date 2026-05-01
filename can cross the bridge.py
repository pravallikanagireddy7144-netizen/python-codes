import sys
data = list(map(int, sys.stdin.read().split()))
X, Y, Z = data[0], data[1], data[2]
max_mangoes = (Z - Y) // X
print(max_mangoes)
