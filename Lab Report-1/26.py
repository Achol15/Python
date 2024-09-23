def find_ascii(char):
    ascii_val = ord(char)
    return ascii_val
char = input("Enter a character: ")
ascii_val = find_ascii(char)
print("The ASCII value of", char, "is", ascii_val)