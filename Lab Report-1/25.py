def convert_decimal_to_all(n):
    binary = bin(n).replace("0b", "")
    octal = oct(n).replace("0o", "")
    hexadecimal = hex(n).replace("0x", "")

    return binary, octal, hexadecimal
decimal_number = 10
binary, octal, hexadecimal = convert_decimal_to_all(decimal_number)

print(f"Decimal: {decimal_number}")
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")