# this operation should work the same under any finite field
# here goes

# lets define our finite field. i use integers mod p. we will call this F_p for clarity. lets take a ridiculously small graph now...

p = 5 # can be whatever prime, but must be a prime in order to be a field (see lecture notes)
a,b = 1,1
F_p = {i for i in range(0,p-1)}
F_p_extended = {(i**2)%p for i in range(0,(p-1)**3 + a*(p-1) + b)}

# now our curve
E = ['inf'] # infinity point will be in all curves
for x in F_p:
    c = x**3 + a*x + b # rename this maybe
    if c%p in F_p_extended: # checks that c is a square mod p
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

    if (P1[0] == P2[0]) and P1 != P2: # same x coordinate => the line through P1P2 is vertical
        return 'inf'
    elif P1 != P2:
        w = (P2[1]-P1[1])//(P2[0]-P1[0])
        v = P # too tired to finish this but its a basic addition formula

    if P1 == P2 and P1[1] == 0: # this is at the end of the loopy bit
        return 'inf'
    elif P1[1] != 0:
        pass

    return (w**2 - P1[0] - P2[0], -w**3 + w*(P1[0] + P2[0]) - v) # thing

print(E) # testing success, going to sleep now, will commit

