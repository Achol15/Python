import math

def solve_quadratic(a, b, c):
    dis = b**2 - 4*a*c
    if dis > 0:
        root1 = (-b + math.sqrt(dis)) / (2*a)
        root2 = (-b - math.sqrt(dis)) / (2*a)
        return root1, root2
    elif dis == 0:
        root = -b / (2*a)
        return root
    else:
        return None
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
roots = solve_quadratic(a, b, c)
if roots is not None:
    if isinstance(roots, tuple):
        print(f"The quadratic equation {a}x^2 + {b}x + {c} = 0 has two real roots: x = {roots[0]} and x = {roots[1]}")
    else:
        print(f"The quadratic equation {a}x^2 + {b}x + {c} = 0 has one real root: x = {roots}")
else:
    print(f"The quadratic equation {a}x^2 + {b}x + {c} = 0 has no real roots (complex roots)")