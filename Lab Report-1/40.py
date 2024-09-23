def is_palindrome(s):
    return s.replace(" ", "").lower() == s.replace(" ", "").lower()[::-1]
input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is not a palindrome.")