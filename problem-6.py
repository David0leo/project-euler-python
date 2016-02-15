"""
Project Euler Problem 6:
Find the difference between the sum of squares
and square of sum of first 100 natural nums.

"""
import time

def sum_squares_n(n):
    #Using known formula for speed
    #Sum squares to n squared
    return ((2*n+1)*(n+1)*n)//6

def sum_squares_n_slow(n):
    #sum squares to n squared by iterating
    return sum([i**2 for i in range(1, n+1)])

def sum_n(n):
    #Using known formula for speed
    #Sum to n
    return ((n+1)*n)//2

def sum_n_slow(n):
    #sum up to n by iterating
    return sum([i for i in range(1, n+1)])

def main():
    """ Get difference of sum of squares 
    vs square of sum of first 100 nat. nums.
    Times different functions to see difference
    in time complexity.
    """
    #setup easy to change value for testing
    #problem wants 100
    N = 100
    
    slow_start = time.clock()
    slow = sum_n_slow(N)**2 - sum_squares_n_slow(N)
    slow_end = time.clock()
    
    fast_start = time.clock()
    fast = sum_n(N)**2 - sum_squares_n(N)
    fast_end = time.clock()
    
    print("Slow answer:", slow)
    print("In", slow_end - slow_start, "seconds")
    print("Fast answer:", fast)
    print("In", fast_end - fast_start, "seconds")
    
    return

main()
