x = float(input("x: "))
y = float(input("y: "))

abs_of_abs = abs(abs(x)- abs(y))
abs_x_y = abs(x - y)

print(f"{abs_of_abs:.4f} ≤ {abs_x_y:.4f}")
