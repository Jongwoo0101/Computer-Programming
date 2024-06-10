year = 0
balance = 1000
while balance < 2000:
    year += 1
    interest = balance * 0.05
    balance += interest
    
print(f'원금의 두배가 되는 기간(년): {year}')
print(f'총액: {balance}')