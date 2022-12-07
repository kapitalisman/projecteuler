numbers = [i + 1 for i in range(100)]
answer = sum(numbers) ** 2 - sum([i ** 2 for i in numbers])
print(answer)
