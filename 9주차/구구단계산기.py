n = int(input("구구단 몇 단을 계산할까? "))
print(f'구구단 {n}단을 계산한다')

for i in range(1, 10, 1):
    print(f'{n} x {i} = {n * i}')