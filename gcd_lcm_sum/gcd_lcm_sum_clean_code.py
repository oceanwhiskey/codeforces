from math import sqrt
import sys

def main():
    read_input_and_solve()


def read_input_and_solve():
    # https://codeforces.com/group/Osuk2cmEQr/contest/426194/problem/B
    t = int(input())
    for _ in range(t):
        x = int(input())
        a, b = solve_GCD_LCM_SUM(x)
        print(a, b)


def solve_GCD_LCM_SUM(x):
    if is_even(x):
        a, b = solution_for_even(x)
    else:
        a, b = solution_for_odd(x)
    return a, b


def is_even(x):
    return x % 2 == 0


def solution_for_even(x):
    a, b = x//2, x//2
    # In this case:
    # gcd(a, b) = a = b = lcm(a, b)
    # and gcd(a, b) - lcm(a, b) = 0
    return a, b


def solution_for_odd(x):
    # x = lcm(a,b) + gcd(a,b)
    # Since gcd divides lcm, gcd must divide x.
    # So any factor of x could potentially be gcd.
    a, b = 1, x-1 # init worst case solution
    for factor in divisor_pairs(odd_divisors_from_1_to_sqrt(x), x):
        lcm, gcd = x-factor, factor # lcm + gcd = x. Note, that x-divisor is also divisible by divisor.
        a, b = find_a_and_b_for_lcm_and_gcd(lcm, gcd, a_init=a, b_init=b)
    return a, b


def find_a_and_b_for_lcm_and_gcd(lcm, gcd, a_init, b_init):
    # lcm*gcd = a*b
    # => (1) lcm/gcd = a/gcd * b/gcd = aa * bb
    # Note, that aa and bb are coprime.
    # We try to find aa as one of the factors of lcm/gcd.
    # Then bb = lcm/gcd/aa and we have to check that gcd(aa, bb) = 1.
    lcm_divided_by_gcd = lcm // gcd
    for aa in divisors_from_sqrt_to_1(lcm_divided_by_gcd): # (2) Note that bb-aa increases with decreasing aa. 
        bb = lcm_divided_by_gcd // aa # follows from (1)
        if gcd*(bb - aa) < b_init - a_init and is_coprime(aa, bb):
            return gcd*aa, gcd*bb # Due to (2) we can shortcircuit here.
    else:
        return a_init, b_init
    

def is_coprime(a, b):
     return calc_gcd(a, b) == 1


def divisors_from_sqrt_to_1(x):
    for y in range(int(sqrt(x)), 0, -1):
        if x % y == 0:
            yield y


def odd_divisors_from_1_to_sqrt(x):
    for y in range(1, int(sqrt(x)) + 1, 2):
        if x % y == 0:
            yield y


def divisor_pairs(stream, x):
    for divisor in stream:
        for y in (divisor, x // divisor):
            yield y


def calc_gcd(a, b):
    if a == 0:
        return b
    return calc_gcd(b % a, a)


if __name__ == '__main__': main()