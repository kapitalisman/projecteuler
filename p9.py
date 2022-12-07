candidates = [(a, b) for a in range(150, 300) for b in range(250, 400) if a < b]
for a, b in candidates:
    c = 1000 - a - b
    if a ** 2 + b ** 2 == c ** 2:
        print(a * b * c)
