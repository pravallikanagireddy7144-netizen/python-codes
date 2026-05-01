c = int(input())
h = c//3600
b = c%3600
m = b//60
s = b%60
print(f'H:M:S-{h}:{m}:{s}')
