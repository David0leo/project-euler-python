# Project Euler Problem 3
###############################
# Find the largest prime factor
# of the number 600851475143
###############################

#checks if a natural number n is prime
#returns boolean
def prime_check(n):
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

#generate a list of primes less than a given value n
def generate_primes(n):
    assert type(n) is int, "Non int passed"
    
    primes = []
    
    if n < 0:
        n *= -1
    if n == 0 or n == 1:
        return primes
    
    for i in range(1, n):
        if prime_check(i):
            primes.append(i)
    
    return primes
    
    
    
    
# Just going to do a simple trial run
def  trial_factor(n):
    assert type(n) is int, "Non-integer passed"
    assert n >= 0, "No negative values allowed"
    
    largest_prime_factor = 0
    primes = generate_primes(int(n**.5) + 1)
    
    for p in primes:
        if n % p == 0:
            if p > largest_prime_factor:
                largest_prime_factor = p
    return largest_prime_factor
    
    
# test    
def main():
    print(trial_factor(600851475143))
    return

main()
    



   
