from sympy import nextprime


prime = 2
answer = 0

while prime < 2e6:
    answer += prime
    prime = nextprime(prime)

print(answer)
