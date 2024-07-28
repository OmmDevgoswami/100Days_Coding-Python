from prettytable import PrettyTable
import PokéData

LOGO = '''
  ____         _           ____              
 |  _ \  ___  | | __  ___ |  _ \   ___  __  __
 | |_) |/ _ \ | |/ / / _ \| | | | / _ \ \ \/ /
 |  __/| (_) ||   < |  __/| |_| ||  __/  >  < 
 |_|    \___/ |_|\_\ \___||____/  \___| /_/\_\ 
                                                  
'''

while True:
  print (LOGO)
  table = PrettyTable()
  print ("Which PokeDex Do You Wanna Access ??")
  print ("'Starter'\t'KentoDex'\t'JhotoDex'\t'HoennDex'\t'SinnohDex'\t'UnovaDex'\t'KalosDex'\t'AlolaDex'")
  I_Choose_You = input("Pick your choice: ").lower()
  table.field_names = ["Pokemon", "Types"]
  table.align["Pokemon"] = "l"
  table.align["Types"] = "c"
  if I_Choose_You == "starter":
    table.add_rows (PokéData.Starter)
  elif I_Choose_You == "kentodex":
    table.add_rows (PokéData.KentoDex)
  elif I_Choose_You == "jhotodex":
    table.add_rows (PokéData.JhotoDex)
  elif I_Choose_You == "hoenndex":
    table.add_rows (PokéData.HoennDex)
  elif I_Choose_You == "sinnohdex":
    table.add_rows (PokéData.SinnohDex)
  elif I_Choose_You == "unovadex":
    table.add_rows (PokéData.UnovaDex)
  elif I_Choose_You == "kalosdex":
    table.add_rows (PokéData.KalosDex)
  elif I_Choose_You == "aloladex":
    table.add_rows (PokéData.AlolaDex)
  else:
    print ("Invalid Choice")
    

  print (table)
  loop = input("Would You like to Explore Another PokeDex Entry ? Yes/No? ").lower()
  if loop == "yes":
    continue
  elif loop == "no":
    print ("Thank You for trying this !! ")
    break