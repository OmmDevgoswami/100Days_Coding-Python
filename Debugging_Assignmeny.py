print("############DEBUGGING#####################")

# 1) Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

def my_function():
  for i in range(1, 21):    #The '20' was changed to '21' as range(m, n`) checks between m and n` = n-1
    if i == 20:             #Changing value to 21 makes this statement "True".
      print("You got it")
my_function()

# 2) Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

print()
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]    # Here the index of the list is from 0 - 5 
dice_num = randint(0, 5)                      # randint(a,b) checks the value inclusive of 'a' and 'b'. 
print(dice_imgs[dice_num])                    # This above debugging stops indexOutOfBound Error

# 3) Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

print()
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:                          #Earlier the Code was unable to print a statement when input = 1994
  print("You are a Gen Z.")

# 4) Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

print()
age = int(input("How old are you? "))       #Type Error : Changed datatype from str -> int
if age > 18:
    print(f"You can drive at age {age}.")    #Indentation Error. #'printf' statement to print variable.

# 5)Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

print()
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))    #Equals('==') operator is chnaged to Assignment('=') operator
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
# mutate([1,2,3,5,8,13])

print()
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)    #Indenting this line will add each value after multiplying to 2 into the new list.
  print(b_list)
  
mutate([1,2,3,5,8,13])