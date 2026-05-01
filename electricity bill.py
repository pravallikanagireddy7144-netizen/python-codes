units = int(input())
if units < 200:
    cost = 1.20
elif units < 400:
    cost = 1.40
elif units < 600:
    cost = 1.60
elif units < 800:
    cost = 1.80
else:
    cost = 2.00

bill = units * cost

if bill > 400:
    surcharge = bill * 0.15
else:
    surcharge = 0

total = bill + surcharge

print("Units Consumed:",units)
print(f"Cost per Unit: {cost:.2f}")
print(f"Bill: {bill:.2f}")
print(f"Surcharge: {surcharge:.2f}")
print(f"Total Amount: {total:.2f}")

