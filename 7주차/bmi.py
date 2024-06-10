kg = int(input("체중(kg): "))
heigt = float(input("키(m): "))

bmi = kg / (heigt * heigt)

print(f'비만도(BMI) : {bmi:.1f}')

if bmi < 18.5:
    print("당신은 저체중입니다.")

elif 18.5 <= bmi < 23.0:
    print("당신은 정상체중 입니다.")
    
elif 23.0 <= bmi < 25.0:
    print("당신은 과체중 입니다.")
    
elif 25.0 <= bmi < 30.0:
    print("당신은 비만 I 입니다.")

elif 30.0 <= bmi < 40.0:
    print("당신은 비만 II 입니다.")

else:
    print("당신은 심각한 비만 III 입니다.")