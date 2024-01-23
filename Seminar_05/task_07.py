import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generator_of_primes(N):
    primes = []
    prime_count = 0
    num = 2
    while prime_count < N:
        if is_prime(num):
            primes.append(num)
            prime_count += 1
        num += 1
    return primes

print(generator_of_primes(8))           