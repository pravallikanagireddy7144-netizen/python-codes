p = int(input())
r = int(input())
t = int(input())
a = (1+(r/100))**t
b = a*p
c = b-p
print(f'{c:.2f}')
