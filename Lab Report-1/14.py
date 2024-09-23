def primes(start, end):
    for num in range(start, end + 1):
        is_prime = True
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
start = 10
end = 50
primes(start, end)