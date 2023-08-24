def get_primes(lst):
    for num in lst:
        divisors = 0
        for div in range(1, num + 1):
            if num % div == 0:
                divisors += 1
        if divisors == 2:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
