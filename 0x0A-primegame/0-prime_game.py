#!/usr/bin/python3

"""
prime game.
"""

def primes(max_num):
    """Return a list of all prime numbers up to max_num using the Sieve of Eratosthenes."""
    if max_num == 0 or max_num == 1:
        return []
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    return [num for num, prime in enumerate(is_prime) if prime]

def isWinner(x, nums):
    """is winner."""
    if x <= 0:
        return None
    ben = maria = 0
    for num in nums:
        if len(primes(num)) % 2 == 0:
            ben += 1
        else:
            maria += 1
    return "Ben" if ben > maria else "Maria"

