line = "*"*60
print(line)
print("당신의 상대적 지방 질량 지수(RFM)을 계산합니다.")
print(line)
name = input("당신의 이름을 입력: ")
gender = int(input("성별 입력(남성이면 0, 여성이면 1): "))
cm = float(input("당신의 키(단위: cm) 입력: "))
inch = int(input("당신의 허리둘레(단위: Inch) 입력: "))
print(line)
rfm = 64 - (20 * (cm / (inch * 2.54))) + 12 * gender
print(f"{name}님의 RFM: {rfm:.2f}%")
