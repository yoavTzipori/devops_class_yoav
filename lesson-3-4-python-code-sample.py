# take input from user and calculate the area
# num1 = int(input("please insert the length :"))
# num2 = int(input("please enter the width :"))
#
# result = num1 * num2
# print(f"the length that you enter is {num1} and the width that you enter is {num2} \n and the are is \n {result}")



# a = int(input("please enter the first number"))
# b = int(input(" please enter the secound number"))
#
# if int(b > a and b> 2 ):
#     print("b is grater then a ")
#     exit()
#
# elif int(a > b or b >a ) :
#     print("a is grater then b ")
#     exit()
#
# elif int(a == b) :
#     print("a is echo to b ")
#
# else :
#     print("syntext error ")
#





# # print choose an option
# print("slect your math operator  \n 1.add \n 2.subtract \n 3.multiply \n 4.divide")
#
# #take an input from the user between 1-4
#
# chioce  = input("please enetr a number between 1 -4 ")
#
# #take from the user 2  flout numbers
# num1 = float(input("please insert the first number"))
# num2= float(input("please insert the secound number"))
#
# # check if the choice is 1 do the adding operation
#
# if chioce == '1' :
#     result = num1 + num2
#     print(f"{num1} + {num2} = {result}")
#




#
# names = []
# for i in range(6) :
#     name = input("please enter a name or type 'exit' to stop " )
#     if name.lower() == 'exit' :
#         break
#     names.aappend(nme)
# print(names)

#
#
# for i in range (1,21) :
#     if i % 2== 0 :
#         print(f"even : {i}\n")
#     else :
#         print(f"not even : {i}\n")

# #### תרגיל 1: הדפסת מספרים מ-1 עד 10
# כתוב לולאת `for` להדפסת המספרים מ-1 עד 10.
#
# for i in range(1,11):
#     print(i)





#
# ### תרגיל 2: סכום של רכיבי רשימה
# בהינתן רשימה של מספרים, חשב והדפס את הסכום של כל הרכיבים ברשימה.
#
# nums = [1,2,3,4,5,6]
# sum = 0
# for num in nums :
#     sum += num
#     print(f"sum = : {sum}")







#
# # ### תרגיל 3: הדפסת מספרים זוגיים
# # כתוב לולאת `for` להדפסת כל המספרים הזוגיים בין 1 ל-20.
#
# for z in range(1,101):
#     if z %2==0:
#         print(f"this is a positive:{z}")



#
# #
# # ### תרגיל 4: הדפסת תווים משרשרת
# # בהינתן מחרוזת, הדפס כל תו בשורה נפרדת.
# str = ["hello" , "world" , "my" , "name" , "is" , "yoav"]
# for i in str :
#     print(f"{i} ")
#




#
# ### תרגיל 5: מציאת המספר הגדול ביותר ברשימה
# בהינתן רשימה של מספרים, מצא והדפס את המספר הגדול ביותר.
# numbers = [12,45,4,6,7,99,9]
# largest_num = numbers[0]
# for num in numbers:
#     if num > largest_num:
#         largest_num = num
# print(largest_num)




# ### תרגיל 7: טבלת כפל
# ייצר והדפס את טבלת הכפל עבור המספרים 1 עד 5
#2 for loops in the same ranges
# my vars i ,j
#print statment inside of the loop
#print new line
#
# for i in range(1,100):
#     for j in range(1,100) :
#         print(f"{i} * {j} = {i*j}")
#     print()



#
# i = 1
# while i < 6 :
#     print(i)
#     i+=1

# i =1
# while i <100 :
#     print('*' * i)
#     i += 1
#
# print("5" * 5)

# import random
# number = random.randint(1,5)
# gussing = 1
# while gussing <=4:
#     guess = int(input("please guess a number from 1 to 10 : "))
#     if guess == number:
#         print(f"you won the number was  - {number}")
#         break
#     gussing +=1
# else :
#     print(f"you lose {number}")
#


# # this loop is print from 1-4
# i =0
# while i < 5 :
#     print(i)
#     i+=1

# user_input = ""
# while user_input != "exit":
#     user_input = input("type exit to stop : ")
#     print(f"you typed {user_input}")


#endless loop
# while not True :
#     print("hello devops class")


# Task: Guess the Number Game
# Write a Python program that uses a while loop to create a simple "guess the number" game. The program should:
# 1.	Generate a random number between 1 and 10.
# 2.	Prompt the user to guess the number.
# 3.	Continue prompting the user until they guess the correct number.
# 4.	Print a congratulatory message when the user guesses correctly.
# Hints:
# •	You can use the random module to generate a random number.
# •	Use a while loop to repeatedly ask for user input until the correct number is guessed.
# •	Compare the user's guess with the generated number and provide feedback.

#
# #import random
# import random
#
# #random number 1- 10
# user_guess = None
# print("please guess a number between 1 - 10 ")
# target_number = random.randint(1,10)
#
# #while loop
# #guess the number with input function
#
# while user_guess != target_number :
#     user_guess = int(input("enetr your guess : "))
# #provide a feedback on the user guses , high/low
#     if user_guess < target_number :
#         print("number is too low")
#     elif user_guess > target_number :
#         print("too high ")
# print(f"you won the number is {target_number}")


# # str_list = ["list" , "str" , "yt"]
# str_list2 = ["hello" , "world" , " this" , "is" , "python" , "class"]
# # string_to_append = "class"
# # str_list2.append(string_to_append)
# # print(str_list2)
# str_to_remove = "hello"
# str_list2.remove(str_to_remove)
# print(str_list2)



#data types in python
# my_list = ["hello"]
# my_di = {"keyvalue":"hello"}
# print(type(my_di))
# print(type(my_list))
# my_tup = (1,2,3,4)
# my_var  = 1
# my_str = "str"
# print(type(my_var))
# print(type(my_str))
# print(type(my_tup))


# python list slicing
# my_slice = ["1","2","3","4","5","6","7","8","9"]
# new_var = my_slice[3:6]
# print(new_var)
# print(my_slice)
#
# my_list = [1,2,3,4,5,6]
# my_list.remove(3)
# my_list.append(3)
# print(my_list)


#tuple is never change!
# my_tuple = (1,2,3,4,5,6,7,8)
# print(my_tuple)
# print(type(my_tuple))

#
# #between key value pairs we use "," and between key and value we use ":"
# dict1 = {"name":"yoav","my_phone_number":84385950504,"city":"rome"}
# print(dict1)









