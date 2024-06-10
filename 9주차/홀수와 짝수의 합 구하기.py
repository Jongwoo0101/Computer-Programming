n = int(input("n의 값을 입력해주세요: "))

odd_sum = 0;
even_sum = 0

for count in range(1, n + 1):
    if count % 2 == 0:
        even_sum += count
    else:
        odd_sum += count
        
print(f'1부터 {count}까지의 짝수합: {even_sum}, 홀수합: {odd_sum}')