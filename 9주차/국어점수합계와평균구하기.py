kor_score = [98, 88, 65, 70, 83, 91, 62, 53, 75, 30]

sum_kor = 0;

for jumsoo in kor_score:
    sum_kor += jumsoo
    
avg_kor = sum_kor / len(kor_score)

print("전체 합계 :", sum_kor)
print("전체 평균 :", avg_kor)