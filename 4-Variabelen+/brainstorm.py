from math import sqrt


def vkv(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant > 0:
        print("Their are two real solutions")
        print("x1 =", (-b + sqrt(discriminant)) / (a * 2))
        print("x2 =", (-b - sqrt(discriminant)) / (a * 2))
    elif discriminant == 0:
        print("x = ", (-b) / (a * 2))
    else:
        print("Their are no real solutions.")


if __name__ == "__main__":
    while True:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        vkv(a, b, c)
        print("------------")
