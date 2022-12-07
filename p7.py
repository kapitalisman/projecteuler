from sympy import nextprime


prime = 1
for i in range(10001):
    prime = nextprime(prime)

print(prime)
