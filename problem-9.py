"""Project Euler Problem 9
Find the Pythagorean triplet for which a+b+c=1000
Find product abc.
Note: a < b < c a^2 + b^2 = c^2
"""

def gen_primal_py_triples(c):
    """Generates Pythagorean triple (a,b,c).
    This function only deals with primal triples
    Args:
        c: an integer which is the bound for the triples
    Returns:
        A list of pythagorean triples (a, b, c) given as a list of 
        tuples with the largest
    """
    assert type(c) is int, "argument non-integer"
    triples = []

    if c <= 0:
        return triples

    for m in range(2, int(c**0.5)):
        if m % 2 == 0:
            n_start = 1
        else:
            n_start = 2
        for n in range(n_start, m):
            if gcd(m, n) == 1:
                triples.append(euclids_formula(m, n))
    return triples

def euclids_formula(m, n):
    """
    """

    assert type(m) is int, ""
    assert type(n) is int, ""
    a = m*m - n*n
    b = 2*m*n
    c = m*m + n*n

    return (min(a, b), max(a, b), c)

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

def main():
    print(gen_primal_py_triples(300))
    return

#for testing
main()
