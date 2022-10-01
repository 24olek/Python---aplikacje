import random
marks = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+[]\{}|;':\",./<>?"
password = ""
for x in range(15):
    i = random.randrange(len(marks))
    password += marks[i]

print(password)
