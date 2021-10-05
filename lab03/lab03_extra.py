""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def is_multiple(i):
        if i ** 2 < n:
            if n % i == 0:
                return False
            else:
                return is_multiple(i+1)
        return True
    return is_multiple(2)


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 10 :
        return 0
    return ten_pairs(n // 10) + count_time(10 - n % 10, n // 10)

def count_time(i,n):
    if n == 0:
        return 0
    if n % 10 == i:
        return count_time(i,n//10) + 1
    return count_time(i, n//10)