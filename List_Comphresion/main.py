value1_list = []
value2_list = []
with open ("List_Comphresion\\file1.txt" , "r") as file:
    value1 = file.readlines()
    value1_list = [int(num.strip()) for num in value1]
    value1_list.sort()
    
with open ("List_Comphresion\\file2.txt" , "r") as file:
    value2 = file.readlines()
    value2_list = [int(num.strip()) for num in value2]
    value2_list.sort()

print (value1_list)
print (value2_list)  
result = [final_val for final_val in value1_list if final_val in value2_list]    

print (result)