fibs = [1, 2]
answer = 2

while fibs[-1] <= 4e6:
    next = fibs[-2] + fibs[-1]
    if next % 2 == 0:
        answer += next
    fibs.append(next)

print(answer)
