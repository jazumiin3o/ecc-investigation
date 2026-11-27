'''

This code performs elliptic curve point addition over a finite field of the form Z\pZ, where p is prime.
Maybe it's worth experimenting more with other finite fields. But cryptographically, this is good enough.

notes:
    - This code could contain multiplication, and use a double-and-add implementation, possibly Pollard-Rho
      as well. I will add this in the future, either in this code, or a separate module.
    - Right now it requires b as an argument despite it not being used in the algorithm. This is just to
      keep it consistent. I might change my mind about this later.
    - The loop condition is kind of funny but it works so long as you want to add every point in the list.
      Again, this is likely to be changed.
    - I may choose to keep this as a binary operation and create a separate haskell fold-like function for
      adding many points in succession.

'''

def add(points, a, b, p):
    from algorithms import inverse
    P1, P2, pointer = points[0], None, 0
    while P2 != points[-1]:
        P2 = points[pointer+1]
        pointer += 1

        # pretty much useless but makes the groupish properties more clear
        if P1 == 'inf':
            P1 = P2
            continue
        if P2 == 'inf':
            P1 = P1 # does nothing lol
            continue
    
        # point addition formulae. these will be better written in the docs, this code is horrendous
        if P1 != P2:
            if P1[0] == P2[0]: # same x coordinate => the line through P1P2 is vertical
                P1 = 'inf'
                continue
            else:
                w = (P1[1]-P2[1])*inverse(P1[0]-P2[0], p) # distinct points general case

        elif P1 == P2: 
            if P1[1] == 0: # this is at the end of the loopy bit
                P1 = 'inf'
                continue
            else: # same point general case
                w = (3*(P1[0])**2 + a)*inverse(2 * P1[1],p) # slope obtained by taking derivative
    
        x = w**2 - P1[0] - P2[0]
        y = w*(P1[0]- x) - P1[1]
        P1 = [x%p, y%p]

    return P1
