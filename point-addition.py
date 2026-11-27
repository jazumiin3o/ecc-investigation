# this operation should work the same under any finite field
def gcd(n,p):
    if n==0:
        return p
    return gcd(p%n, n) # recursion hehehehehehe

# extended euclidean.. to be improved
def inverse(n, p):
    n = n%p
    if gcd(n,p) != 1:
        return -1
    p0 = p # saving original p for later in case result is negative
    y = 0
    x = 1
    if p == 1:
        return 0 # all numbers mod 1 are 0 so their inverses are too.
    while n > 1:
        q = n//p
        t = p
        p = n%p
        n = t
        t = y

        y = x - q*y
        x = t

    if x < 0:
        x = x + p0
    return x

# now our curve
def generate_curve(a,b,p):
    # lets define our finite field. i use integers mod p. we will call this F_p for clarity.
    F_p = {i for i in range(0,p)} # this only goes up to p-1
    p_quadratic_residues = {i**2 for i in range(0,p)} # list of quadratic residues modulo p
    E = ['inf'] # infinity point will be in all curves
    for x in F_p:
        c = x**3 + a*x + b # rename this maybe
        for square in p_quadratic_residues:
            if square%p == c%p:# checks that c is a square mod p
                y = int(math.sqrt(square)) % p
                E.append([x,y%p])
                E.append([x,(-y)%p])
                break # stops duplicate points

    return E

# time for the fun stuff
def add(points, a, b, p): # if only i had access to haskell fold... might make this a magic method instead
    P1, P2, pointer = points[0], None, 0
    while P2 != points[-1]:
        P2 = points[pointer+1]
        pointer += 1

        # pretty much useless but makes the groupish properties more clear
        if P1 == 'inf':
            P1 = P2
        elif P2 == 'inf':
            P1 = P1 # does nothing lol just moves to the next iteation, maybe continue is better
    
        # point addition formulae. these will be better written in the docs, this code is horrendous
        elif (P1[0] == P2[0]) and P1 != P2: # same x coordinate => the line through P1P2 is vertical
            P1 = 'inf'
        elif P1 != P2: # regular case, distinct points yay
            w = (P1[1]-P2[1])*inverse(P1[0]-P2[0], p)
        elif P1 == P2 and P1[1] == 0: # this is at the end of the loopy bit
            P1 = 'inf'
        elif P1[1] != 0: # same point
            w = (3*(P1[0])**2 + a)*inverse(2 * P1[1],p) # slope obtained by taking derivative
    
        x = w**2 - P1[0] - P2[0]
        y = w*(P1[0]- x) - P1[1]
        P1 = [x%p, y%p]

    return P1

a, b, p = 497, 1768, 9739
PPQR = [[493,5564], [493,5564], [1539,4742], [4403, 5202]]
print("S =", add(PPQR, a, b, p))

