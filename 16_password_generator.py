import random

length = 16

password = []
for i in range(0, length):
    password.append(chr(random.randint(32, 126)))

print("".join(password))

