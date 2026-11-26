# this operation should work the same under any finite field
# here goes
def gcd(n,p):
    if n==0:
        return p
    return gcd(p%n, p) # recursion hehehehehehe

def inverse(n, p):
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

# lets define our finite field. i use integers mod p. we will call this F_p for clarity. lets take a ridiculously small graph now...
global a,b,p
p = 9739 # can be whatever prime, but must be a prime in order to be a field (see lecture notes)
import math
# i'll probably turn this into a library module at some point and remove preset a,b and p
a,b = 497,1768
F_p = {i for i in range(0,p)} # this only goes up to p-1
p_quadratic_residues = {i**2 for i in range(0,p)} # list of quadratic residues modulo p

# now our curve
E = ['inf'] # infinity point will be in all curves
for x in F_p:
    c = x**3 + a*x + b # rename this maybe
    for square in p_quadratic_residues:
        if square%p == c%p:# checks that c is a square mod p
            y = int(math.sqrt(square)) % p
            E.append([x,y%p])
            E.append([x,(-y)%p])

# time for the fun stuff
def add(P1,P2):
    # pretty much useless but makes the groupish properties more clear
    if P1 == 'inf':
        return P2
    if P2 == 'inf':
        return P1
    
    # point addition formulae. these will be better written in the docs, this code is horrendous
    if (P1[0] == P2[0]) and P1 != P2: # same x coordinate => the line through P1P2 is vertical
        return 'inf'
    elif P1 != P2: # regular case, distinct points yay
        w = (P1[1]-P2[1])*inverse(P1[0]-P2[0], p)

    if P1 == P2 and P1[1] == 0: # this is at the end of the loopy bit
        return 'inf'
    elif P1[1] != 0: # same point
        w = (3*(P1[0])**2 + a)*inverse(2 * P1[1],p) # slope obtained by taking derivative
    
    x = w**2 - P1[0] - P2[0]
    y = w*(P1[0]- x) - P1[1]
    return[x%p, y%p]

print(E) # testing success, going to sleep now, will commit
print(add([5274,2841], [8669, 740]))

