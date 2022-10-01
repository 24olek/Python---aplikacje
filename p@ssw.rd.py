#Generates password of fifteen characters
import random
marks = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+[]\{}|;':\",./<>?"
password = ""
inp = ""
while inp != "exit":
    for x in range(15):
        i = random.randrange(len(marks))
        password += marks[i]
    print(password)
    password = ""
    inp = input("For exit, write 'exit'").lower()
