def check_odd_even(n):
    
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
print(check_odd_even(num))