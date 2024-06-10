sales = int(input("구입 금액을 입력하시요: "))
if sales >= 100000:
    discount = sales * 0.05
    sales = sales - discount
    
print("지불 금액은 ", sales, "입니다.") 