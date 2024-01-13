from math import sqrt

def calc_gcd(a, b):
    if a == 0:
        return b
    return calc_gcd(b % a, a)

t = int(input())
for _ in range(t):
    x = int(input())
    if x % 2 == 0:
        aa, bb = x//2, x//2
    else:
        aa, bb = 1, x-1
        for y in (y for y in range(1, int(sqrt(x)) + 1, 2) if x % y == 0):
            for c in (c for c in (y, x // y) if c < x):
                lcm, gcd = x-c, c
                s = lcm // gcd
                for a in (a for a in range(int(sqrt(s)), 0, -1) if s % a == 0):
                    b = s // a
                    if gcd*(b - a) < bb - aa and calc_gcd(a, b) == 1:
                        aa, bb = gcd*a, gcd*b
        print(aa, bb)