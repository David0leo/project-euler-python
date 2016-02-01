# Project Euler Problem 5
######################################
# Find smallest pos number that is
# evenly divisible by all numbers from
# 1 to 20
######################################

#essentially getting the lcm of several numbers
# formula for lcm is lcm(a,b) = a*b / gcd(a,b)

def gcd(a, b):
    assert type(a) is int, "arg1 non int"
    assert type(b) is int, "arg2 non int"
    #just do Euclidean algorithm
    if a < b:
        while a:
            b, a = a, b%a
        return b
    else:
        while b:
            a, b = b, a%b
        return a

def gcd_test():
    print(gcd(1, 1))
    print(gcd(5, 35))
    print(gcd(21, 56))
    print(gcd(27, 9))
    return

def lcm(a, b):
    return a*b//gcd(a,b)

def mult_lcm(num_list):
    #initialize prev
    prev = 1
    for i in range(0, len(num_list) - 1):
        if i == 0:
            a = num_list[0]
        b = num_list[i+1]
        a = lcm(a, b)
    
    return a

def main():
    print(mult_lcm(range(1, 21)))
    return

#test
main()
    
