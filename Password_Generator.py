import random

print ("Welcome to the Strong Password Generator !!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like?  "))
nr_numbers = int(input(f"How many numbers would you like? "))

password = ""
#Easy Level
for i in range(0,nr_letters):
    password += random.choice(letters)
for i in range(0, nr_numbers):
    password += random.choice(numbers)
for i in range(0,nr_symbols):
    password += random.choice(symbols)
print(f"Hers's Your Easy Password: {password}")

#Hard Level
password_list = []
for i in range(0,nr_letters):
    password_list += random.choice(letters)
for i in range(0, nr_numbers):
    password_list += random.choice(numbers)
for i in range(0,nr_symbols):
    password_list += random.choice(symbols)
password_hard = ""
random.shuffle(password_list)
for i in range (0, len(password_list)):
    password_hard += password_list[i]
print("Here's a Stronger and Better password:",password_hard)