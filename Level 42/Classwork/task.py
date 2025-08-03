def no_boring_zeros(n):
    while n != 0 and n % 10 == 0:
        n //= 10
    return n





def is_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b



def array_diff(a, b):
    return [x for x in a if x not in b]
