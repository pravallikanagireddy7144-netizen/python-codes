n = int(input())
a = n//10
b = n%10
c = b//5
if n%10==0:
    print(n//10)
elif n%10!=0 and n%5==0:
    print(a+c)
else:
    print(-1)
