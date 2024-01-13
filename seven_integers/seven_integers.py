from functools import reduce


def main():
    # https://codeforces.com/gym/102979/problem/J
    n = int(input())
    a = list(map(int, input().split()))
    # a = [6, 5, 3, 2, 2, 2, 2, 2]
    # a = [6, 5, 3, 2, 2, 2, 2, 1]
    # n = len(a)
    print(refactored(a))
    

def refactored(a):
    n = len(a)
    a.sort(reverse=True)

    sums_of_last_four_prices_minus_third = calc_sums_of_last_four_elements_minus_third(a)
    max_sums_of_last_four_prices_minus_third = calc_max_sums_of_last_four_elements_minus_third(sums_of_last_four_prices_minus_third, n)
    
    result = -1    

    for i1 in range(n-6):
        i2, i3 = i1+1, i1+2
        while ( first_inequality_met(a, i1, i2, i3) and
            i2_within_bounds(i2, n) and
            not result_found(result) ):

            while ( first_inequality_met(a, i1, i2, i3) and
                i3_within_bounds(i3, n) and
                not result_found(result) and
                second_inequality_possible(a, max_sums_of_last_four_prices_minus_third, i2, i3) ):
                if second_inequality_met(a, sums_of_last_four_prices_minus_third, i2, i3):
                    result = a[i1] + a[i2] + 2*a[i3] + sums_of_last_four_prices_minus_third[i3]
                i3 += 1

            i2, i3 = i2+1, i2+2
        if result_found(result):
            break
    return result


def second_inequality_possible(a, sums_of_five_max, i2, i3):  
    return a[i2] < sums_of_five_max[i3]


def second_inequality_met(a, sums_of_five, i2, i3):
    return a[i2] < sums_of_five[i3]


def i2_within_bounds(i2, n):
    return i2 < n-5


def i3_within_bounds(i3, n):
    return i3 < n-4


def first_inequality_met(a, i1, i2, i3):
    return a[i1] < a[i2] + a[i3]    


def result_found(result):
    return result >= 0


def calc_sums_of_last_four_elements_minus_third(a):
    n = len(a)
    first_sum = sum(map(a.__getitem__, range(1,5))) - a[0]
    sums = [first_sum]
    for i in range(1,n-4):
        first_sum = first_sum + a[i-1] - 2*a[i] + a[i+4]
        sums.append(first_sum)    
    return sums


def append_max_to_sums_max(sums_max, sum):
    sums_max.append(max(sums_max[len(sums_max)-1], sum))
    return sums_max


def list_with_last_element(non_empty_list):
    return [non_empty_list[len(non_empty_list)-1]]


def calc_max_sums_of_last_four_elements_minus_third(sums_of_last_four_elements_minus_third, n):
    reversed_tail_of_sums = list(reversed(sums_of_last_four_elements_minus_third[0:-1]))
    reversed_max_sums = reduce(append_max_to_sums_max, reversed_tail_of_sums, list_with_last_element(sums_of_last_four_elements_minus_third))
    return list(reversed(reversed_max_sums))


if __name__ == '__main__': main()
