from collections import Counter
import math
from p3 import get_prime_factors


all = Counter()

for i in range(20):
    factors = get_prime_factors(i + 1)
    all = all | Counter(factors)

answer = math.prod([k ** v for k, v in all.items()])
print(answer)
