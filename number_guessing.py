


import random
choice = random.randint(1,4)
num = 1
while num <= 4:
    choice = int(input("please insert a number between 1 to 10: "))
    if num == choice:
        print(f"you won! the number was {choice}")
        break
    num += 1
else:
    print(f"you lost :( {choice}")
