total = 0

for n in range(1, 101, 2):
    total += n
    if total > 1000:
        break
print(f'1 + 3 + ... + {n - 2} = {total - n}')