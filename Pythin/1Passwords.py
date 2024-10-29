import random
import string
length = input("How long do you want your password? ")
length = int(length)
amount = input("How many passwords? ")
amount = int(amount)
passwords = []
i = 0 
while i < amount:
    password  = ''.join(random.choice(string.ascii_letters) for x in range(length))
    str(password)
    passwords.append(password)
    i += 1
print(passwords)

