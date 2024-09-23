def find_armstrong(lower, upper):
    armstrong_numbers = []
    for num in range(lower, upper + 1):
        num_str = str(num)
        num_len = len(num_str)
        sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
        if sum_of_powers == num:
            armstrong_numbers.append(num)
    return armstrong_numbers

start = 100
end = 500
armstrong_numbers = find_armstrong(start, end)
print(f"Armstrong numbers between {start} and {end} are: {armstrong_numbers}")