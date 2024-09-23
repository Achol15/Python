def calculate_power(base, exponent):
    result = base ** exponent
    return result
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = calculate_power(base, exponent)
print(result)