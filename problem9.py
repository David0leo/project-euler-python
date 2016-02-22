"""Project Euler Problem 9
Find the Pythagorean triplet for which a+b+c=1000
Find product abc.
Note: a < b < c a^2 + b^2 = c^2
"""

def gen_primal_py_triples(bound):
    """Generates Pythagorean triple (a,b,c).
    This function only deals with primal triples
    Args:
        bound: an integer which is the bound for the triples
               max c is < (2*bound)**2
    Returns:
        A list of pythagorean triples (a, b, c) given as a list of 
        tuples with the largest
    """
    assert type(bound) is int, "argument non-integer"
    triples = []

    if bound <= 0:
        return triples

    for m in range(2, bound):
        if m % 2 == 0:
            n_start = 1
        else:
            n_start = 2
        for n in range(n_start, m):
            if gcd(m, n) == 1:
                triples.append(euclids_formula(m, n))
    return triples

def gen_triple_set(primal_triple, bound):
    triple_set = []
    for i in range(1, bound//primal_triple[2]):
        a = primal_triple[0] * i
        b = primal_triple[1] * i
        c = primal_triple[2] * i
        triple_set.append((a, b, c))
    return triple_set
    

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
    gen_bound = 10
    found = False
    primal_triples = gen_primal_py_triples(gen_bound)
    last = (0, 0, 0)
    
    while not found:
        last = primal_triples[-1]
        gen_bound *= 2
        primal_triples = gen_primal_py_triples(gen_bound)
        if gen_bound > 50:
            break        
        for primal in primal_triples:
            triples = gen_triple_set(primal, 1000)
            for i in range(len(triples) - 1, -1, -1):
                triple = triples[i]
                if triple[0] == last[0] and triple[1] == last[1] and triple[2] == last[2]:
                    break
                sum_triple = triple[0] + triple[1] + triple[2]
                print(sum_triple)
                if sum_triple == 1000:
                    print("triple (a, b, c) =", triple)
                    print(triple[0] * triple[1] * triple[2])
                    found = True
                    return
        
    return

main()
    
