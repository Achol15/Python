def is_armstrong(n):
    str_n = str(n)
    num_digits = len(str_n)
    sum_cubes = sum(int(digit) ** num_digits for digit in str_n)
    return sum_cubes == n
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")