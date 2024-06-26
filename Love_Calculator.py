print("The Love Calculator is calculating your score...")
name1 = input("Enter the First Lover's name: ") # What is your name?
name2 = input("Enter the Second Lover's name: ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
T = name1.count("t")
T += name2.count("t")
R = name1.count("r")
R += name2.count("r")
U = name1.count("u")
U += name2.count("u")
E = name1.count("e")
E += name2.count("e")
total_1 = T+R+U+E
L = name1.count("l")
L += name2.count("l")
O = name1.count("o")
O += name2.count("o")
V = name1.count("v")
V += name2.count("v")
total_2 = L+O+V+E
score = str(total_1) + str(total_2)
score = int(score)
if(score < 10 or score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif(score > 40 and score < 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")