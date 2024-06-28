line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?") 


#Brute Force Approach
# if (position[0] == "A"):
#   if (position[1] == "1"):
#     map[0][0] = "X"
#   elif (position[1] == "2"):
#     map[1][0] = "X"
#   elif (position[1] == "3"):
#     map[2][0] = "X"
# elif (position[0] == "B"):
#   if (position[1] == "1"):
#     map[0][1] = "X"
#   elif (position[1] == "2"):
#     map[1][1] = "X"
#   elif (position[1] == "3"):
#     map[2][1] = "X"
# else:
#   if (position[1] == "1"):
#     map[0][2] = "X"
#   elif (position[1] == "2"):
#     map[1][2] = "X"
#   elif (position[1] == "3"):
#     map[2][2] = "X"


#Optimal Approach
pos_1 = position[0].lower()
abc = ["a","b","c"]
index_1 = abc.index(pos_1)
index_2 = int(position[1]) - 1
map[index_2][index_1] = "X"

print(f"{line1}\n{line2}\n{line3}")