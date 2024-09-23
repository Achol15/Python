def fibonacci(n):
    s = [0, 1]
    while len(s) < n:
        s.append(s[-1] + s[-2])
    return s

n = int(input("Enter the number of terms: "))
print(fibonacci(n))