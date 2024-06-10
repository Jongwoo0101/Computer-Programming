time = int(input("근무시간을 입력하시오: "))
money = int(input("시간당 임금을 입력하시오: "))

if time > 40:
    overtime = time - 40
    money = int(money*40 + (1.5*money) * overtime)
else:
    money = money * time
    
print(f'총 임금은{money}원 입니다')