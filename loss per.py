cp, sp = map(float, input().split())
loss = cp - sp
loss_percentage = (loss / cp) * 100
print(format(loss_percentage, ".2f"))
