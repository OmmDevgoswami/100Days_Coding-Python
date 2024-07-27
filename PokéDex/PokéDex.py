from prettytable import PrettyTable
import PokéData

LOGO = '''
  ____         _           ____              
 |  _ \  ___  | | __  ___ |  _ \   ___  __  __
 | |_) |/ _ \ | |/ / / _ \| | | | / _ \ \ \/ /
 |  __/| (_) ||   < |  __/| |_| ||  __/  >  < 
 |_|    \___/ |_|\_\ \___||____/  \___| /_/\_\ 
                                                  
'''
print (LOGO)

table = PrettyTable()
print ("Which PokeDex Do You Wanna Access ??")
print ("'Starter'\t'KentoDex'\t'JhotoDex'\t'HoennDex'\t'SinnohDex'\t'UnovaDex'\t'KalosDex'\t'AlolaDex'")
I_Choose_You = input("Pick your choice: ").lower()
table.field_names = ["Pokemon", "Types"]
if I_Choose_You == "starter":
  table.add_rows (PokéData.Starter)
  table.align["Pokemon"] = "l"
  table.align["Types"] = "c"
print (table)