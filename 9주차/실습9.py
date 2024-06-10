'''
for x in range(5):
    print("환영합니다.")
    
for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(x, end=" ")
    

for i in range(0, 10, 1):
    print("hello")
    2
for i in 'kangnam':
    print(i, end=' ')
    
city = ['서울', '부산', '대구']
no = 10
for i in city:
    no += 1
    print('도시 ', no, ':', i)
    
city = ['서울', '부산', '대구']

for j in range(1, len(city) +  1):
    print('도시', j, ':', city[j-1])
    

'''

password = ""
while password != "computerprogrammingisfun":
    password = input("암호를 입력하시오: ")
    
print("로그인 성공")