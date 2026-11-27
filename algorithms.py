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
    x = [1,0]
    if p == 1:
        return 0 # all numbers mod 1 are 0 so their inverses are too.
    while n > 1:
        q = n//p
        t = p
        p = n%p
        n = t
        t = x[1]

        x[1] = x[0] - q*x[1]
        x[0] = t

    if x[0] < 0:
        x[0] = x[0] + p0
    return x[0]
