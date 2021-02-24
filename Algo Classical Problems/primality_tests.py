"""
Algorithms to create lists of primary numbers
"""

def seive_of_eratosthenes(n):
    """
    A powerful yet simple algorithm to calculate primes

    TODO: Calculate the runtime & space for this algorithm
    """

    # start with a list of primes
    # this follows a greedy approach
    primes = []

    # 2 is the first prime
    number_curr = 2
    
    while True:

        # check with the current list of primes
        is_prime = True
        for prime_number in primes:
            if number_curr % prime_number == 0:
                is_prime = False
                break

        # update the list of primes
        if is_prime:
            primes.append(number_curr)

        # if we reach the nth term, we break from the loop
        if len(primes) == n:
            break

        number_curr += 1

    return primes[-1]

def is_prime(n: int) -> bool:
    """A function to check if the given number is a prime"""
    if n == 1:
        return False

    elif n < 4:
        return True

    elif n % 2 == 0:
        return False

    elif n < 9:
        return True

    elif n % 3 == 0:
        return False

    else:
        # All primes greater than 3 can be written in form - 6k+1/6k-1
        # this simple formula is key to a faster algorithm to detect primes

        # TODO: Why this limit?
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:

            # TODO: why this condition?
            if n % f == 0:
                return False

            # TODO: why this condition?
            if n % (f + 2) == 0:
                return False

            f += 6

    return True

def method_using_primality_test(limit: int) -> int:
    count = 1
    number = 1
    while count < limit:
        number += 2
        if is_prime(number):
            count += 1

    return number
     
