def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_numbers_in_range(minimum, maximum):
    prime_list = []
    for num in range(minimum, maximum + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

minimum = 10
maximum = 30
prime_list = prime_numbers_in_range(minimum, maximum)
print(prime_list)