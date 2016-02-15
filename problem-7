""" Project Euler Problem 7:
Find the 10 001st prime.

Related Problems: 3
"""

def prime_check(n):
    """Checks if natural number n is prime.
    Args:
        n: integer value > 0.
    Returns:
        A boolean, True if n prime and False otherwise.
    """
    
    assert type(n) is int, "Non int passed"
    assert n > 0, "No negative values allowed, or zero"
    
    if n == 1:
        return False
    i = 2
    
    while i*i < n + 1:
        if n != i and n % i == 0:
            return False
        i += 1
    
    return True

def gen_nth_prime(n):
    """Generates the nth prime.
    Args:
        n: integer value > 1.
    Returns:
        The nth prime number.
    """
    
    assert type(n) is int, "Non int as argument"
    assert n > 0, "Arument must be greater than 0 int"
    
    prime_count = 0
    #start checking primes at 2
    #increment i at start of loop so initialize as 1
    i = 1
    
    while prime_count < n:
        i += 1
        #first check is 2, last check is nth prime
        if prime_check(i):
            prime_count += 1
    return i

def main():
    print(gen_nth_prime(10001))
    
    return

#for test
main()
