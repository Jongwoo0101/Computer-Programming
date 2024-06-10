gcd = 1
step = 2

num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))

while step <= num1 and step <= num2:
    if num1 % step == 0 and num2 % step == 0:
        gcd = step
    
    step += 1
    
print('최대공약수: ', gcd)