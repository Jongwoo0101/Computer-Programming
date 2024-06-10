sentinel = -1

scores = []

print('종료하려면 -1을 입력하시오.')

num = float(input('성적을 입력: '))

while num != sentinel:
    scores.append(num)
    num = float(input('성적을 입력: '))
    
if len(scores) > 0:
    print(f'평균은 : {sum(scores) / len(scores)}')
    
else:
    print("입력받은 성적이 없습니다.")