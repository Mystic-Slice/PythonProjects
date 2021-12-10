import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "(){}[],.<>/?\\|=+-_\'\";:!@#$%^&*"

lst = [False,False,False,False]

security = int(input("How secure do you want your password to be in a scale of 1-4?"))
for i in range(security):
    lst[i] = True
    
all = ""

if lst[0]:
    all += lowercase_letters
if lst[1]:
    all += uppercase_letters
if lst[2]:
    all += digits
if lst[3]:
    all += symbols

length = int(input("Enter the length of the password required: "))
amount = int(input("Enter the number of passwords required: "))

for x in range(amount):
    password = ""
    for i in range(length):
        password += random.choice(all)
    print(password)