import random

def genPass():
    alphabet = "abcdfghijklmnopqrstuvwxyz0123456789"
    password = ""
    
    for i in range(6):
        password += random.choice(alphabet)
    return password
print(genPass())
print(genPass())
print(genPass())
