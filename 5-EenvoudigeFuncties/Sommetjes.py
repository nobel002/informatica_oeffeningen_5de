a = int(input("a: "))
b = int(input("b: "))

for i in range(5):
    print(f"{a*(10**i):>6d} + {b*(10**i):<6d} = {a*(10**i) +b*(10**i)}")
