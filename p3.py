from sympy import nextprime


def get_prime_factors(n):
    factors = []
    prime = 2

    while n != 1:
        if n % prime == 0:
            factors.append(prime)
            n /= prime
        else:
            prime = nextprime(prime)
    return factors


if __name__ == "__main__":
    num = 600851475143
    factors = get_prime_factors(num)
    print(factors[-1])
