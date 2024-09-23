def triangle_area(base, height):
    area = 0.5 * base * height
    return area

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = triangle_area(base, height)
print("The area of the triangle is:", area)