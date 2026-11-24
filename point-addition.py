# this operation should work the same under any finite field
# here goes

# lets define our finite field. i use integers mod p. we will call this F_p for clarity. lets take a ridiculously small graph now...
global a,b,p
p = 37 # can be whatever prime, but must be a prime in order to be a field (see lecture notes)
# i'll probably turn this into a library module at some point and remove preset a,b and p
a,b = 0,7
F_p = {i for i in range(0,p)} # this only goes up to p-1
p_quadratic_residues = {(i**2)%p for i in range(0,p)} # list of quadratic residues modulo p

# now our curve
E = ['inf'] # infinity point will be in all curves
for x in F_p:
    c = x**3 + a*x + b # rename this maybe
    if c%p in p_quadratic_residues: # checks that c is a square mod p
        y = c % p
        E.append([x,y])
        E.append([x,-y])

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
        w = (P1[1]-P2[1])//(P1[0]-P2[0])%p # slope probably needs extended euclidean algo

    if P1 == P2 and P1[1] == 0: # this is at the end of the loopy bit
        return 'inf'
    elif P1[1] != 0: # same point
        w = (((3*(P1[0])**2 + a)//2)//P1[1])%p # slope obtained by taking derivative
    
    x = (w**2 - P1[0] - P2[0])%p
    y = (w*(P1[0]- x) - P1[1])%p
    return(x, y) 

print(E) # testing success, going to sleep now, will commit
print(add(E[2],E[3]))

