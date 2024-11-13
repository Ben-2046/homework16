print("solve ax^2 + bx + c = 0 a,b,c are integers")
a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
delta = b**2 - 4*a*c

if a == 0:
    print("a cannot be 0")
elif delta > 0:
    print("2roots are", (-b - delta ** 0.5) / (2 * a), "and", (-b + delta ** 0.5) / (2 * a))
elif delta == 0:
    print("1 root is", (-b) / (2 * a))
elif delta < 0:
    print("no real roots")
else:
    print("error")

quit()