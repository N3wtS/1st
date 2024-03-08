import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

num = int(input("Ingresa la longitud:"))

password = ""

for i in range(num):
    password += random.choice(caracteres)

print(password)
