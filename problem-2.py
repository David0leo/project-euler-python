# Project Euler Problem 2
######################################
# ** Find the sum of even Fib. Numbers
#    not greater than four million
######################################

# Fibonacci numbers f(n), starting with f(1) = 1
def fib(n):
    assert type(n) is int, "n is not an integer"
    assert n > 0, "Strictly positive values only allowed"
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

def main():
    current = 0
    sum = 0
    i = 1
    while current < 4000000:
        current = fib(i)
        if current % 2 == 0:
            sum += current
        i += 1
    
    return sum

# test
print(main())
    
