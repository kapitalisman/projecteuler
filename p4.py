all = [i * j for i in range(100, 1000) for j in range(100, 1000)]
all.sort(reverse=True)

for p in all:
    if str(p) == str(p)[::-1]:
        print(p)
        break
