import sys
import math
import decimal


N = int(sys.stdin.readline())

# use the chunovsky law
# break down of the fromual https://www.craig-wood.com/nick/articles/pi-chudnovsky/

'''

1/pi = 12(inf sigma k = 0) ((-1)^k (6k)! (13591409 + 545140134k) / (3k)! (k!)^3 (640320)^(3k + 3/2)

take out the long power of (3k + 3/2)

1/pi = 12 / (640320(sqr_root(640320)) (inf sigma k = 0) ((-1)^k (6k)! (13591409 + 545140134k) / (3k)! (k!)^3 (640320)^(3k)

1/pi = 12 / (426880(sqr_root(10005)) (inf sigma k = 0) ((-1)^k (6k)! (13591409 + 545140134k) / (3k)! (k!)^3 (640320)^(3k)

a = (inf sigma k = 0) ((-1)^k (6k)! / (3k)! (k!)^3 (640320)^(3k)

b = (inf sigma k = 0) ((-1)^k (6k)!k / (3k)! (k!)^3 (640320)^(3k)

pi = (426880(sqr_root(10005)) / (13591409a + 545140134b)

however b is just a * k

instead of calculating a each time, we can use memroy and build a off that
'''


def sqrt(n, one):
    """
    Return the square root of n as a fixed point number with the one
    passed in.  It uses a second order Newton-Raphson convergence.  This
    doubles the number of significant figures on each iteration.
    """
    # Use floating point arithmetic to make an initial guess
    floating_point_precision = 10 ** 16
    n_float = float((n * floating_point_precision) // one) / floating_point_precision
    x = (int(floating_point_precision * math.sqrt(n_float)) * one) // floating_point_precision
    n_one = n * one
    while 1:
        x_old = x
        x = (x + n_one // x) // 2
        if x == x_old:
            break
    return x


def pi(num):
    k = 1
    ak = num
    a = num
    b = 0


    '''a = (inf sigma k = 0) ((-1)^k (6k)! / (3k)! (k!)^3 (640320)^(3k)

b = (inf sigma k = 0) ((-1)^k (6k)!k / (3k)! (k!)^3 (640320)^(3k)

pi = (426880(sqr_root(10005)) / (13591409a + 545140134b)'''
