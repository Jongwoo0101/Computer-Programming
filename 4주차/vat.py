TAX_RATE = 0.075 #세율
price = int(input('물건 값 입력: '))
tax = round(price * TAX_RATE, 2)
print('부가가치세 :', tax, '원')