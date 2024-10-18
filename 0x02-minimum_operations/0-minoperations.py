#!/usr/bin/python3
"""
   0-minoperations
"""
def minOperations(n):
    """
    Calculate the minimum number of operations to get n H characters
    using only 'Copy All' and 'Paste'.
    """
    if n <= 1:
        return 0  # Impossible to achieve if n <= 1

    operations = 0
    divisor = 2

    # Factorize n, and for each factor, add the appropriate number of operations
    while n > 1:
        # While n is divisible by the current divisor, divide it and count the operations
        while n % divisor == 0:
            operations += divisor  # Add the divisor to operations (Copy + multiple pastes)
            n //= divisor
        divisor += 1  # Move to the next potential divisor

    return operations
