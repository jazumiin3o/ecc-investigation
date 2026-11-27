'''

This code generates points on an elliptic curve over a finite field of the form Z\pZ, where p 
is prime.

notes:
    - The time and space complexity of this algorithm is extremely flawed and will be improved (hopefully).
      at the moment, I am not sure how to get around generating the residues as a dictionary, as I need to
      preserve the square itself along with its value mod p, so that I may square root it. The dictionary
      contains many redundant values, but stripping them is O(n) so I try and avoid adding time, as it is
      already very slow! Adding a value to the curve has a complexity of O(n^2) worst case. Not ideal. But,
      some more research should help. I have attemped to delete some variables and garbage collect to free
      some memory, though :)
    - I am aware that math.sqrt adds unnecessary floating point stuff. I will probably write my own integer
      square rooting algorithm (Babylonian) when I am bothered. The numbers should all be perfect squares 
      anyway.
    - Aside from that, the algorithm works as intended, and has been tested using several known values.

'''

def generate_curve(a,b,p):
    from algorithms import inverse, gcd
    import math, gc

    # lets define our finite field. i use integers mod p. we will call this F_p for clarity.
    F_p = {i for i in range(0,p)}# this only goes up to p-1

    keys = [i**2 for i in range(0,p)]
    vals = [k%p for k in keys]
    p_quadratic_residues = dict(zip(keys, vals))

    del keys, vals
    gc.collect() # freeing space lol

    E = {'inf'} # infinity point will be in all curves

    for x in F_p:
        c = x**3 + a*x + b # rename this maybe
        match = next((key for key, val in p_quadratic_residues.items() if val == c%p), None)
        if match is not None:
            y = int(math.sqrt(match))
            E.add((x,y%p))
            E.add((x,(-y)%p))

    return E
