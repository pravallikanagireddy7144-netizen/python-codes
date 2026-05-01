p,c,b,m,s = map(int, input().split())
a = ((p+c+b+m+s)/500)*100
if a>=90:
    print("Grade A")
elif a>=80:
    print("Grade B")
elif a>=70:
    print("Grade C")
elif a>=60:
    print("Grade D")
elif a>=40:
    print("Grade E")
else:
    print("Grade F")
