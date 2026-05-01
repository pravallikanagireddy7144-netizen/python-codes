n, m = map(int, input().split())
online_price = n - (0.10 * n)
if online_price < m:
    print("ONLINE")
elif online_price > m:
    print("DINING")
else:
    print("EITHER")
