amount = int(input("eerste n getallen met n= "))

f_prev = 1
f_current = 1

for i in range(2, amount):
    new = f_prev + f_current
    f_prev, f_current = f_current, new

print(f_current)
