from prettytable import PrettyTable

LOGO = '''
  ____         _                                  
 |  _ \  ___  | | __  ___  _ __ ___    ___   _ __  
 | |_) |/ _ \ | |/ / / _ \| '_ ` _ \  / _ \ | '_ \ 
 |  __/| (_) ||   < |  __/| | | | | || (_) || | | |
 |_|    \___/ |_|\_\ \___||_| |_| |_| \___/ |_| |_|
                                                  
'''
print (LOGO)

table = PrettyTable()
table.field_names = ["Pokemon", "Types"]
table.add_rows ([
    # Kento
    ["Bulbasaur" , "Grass - Poison"],
    ["Ivysaur" , "Grass - Poison"],
    ["Venusaur" , "Grass - Poison"],
    ["Charmander" , "Fire"],
    ["Charmeleon" , "Fire"],
    ["Charizard" , "Fire - Flying"],
    ["Squirtle" , "Water"],
    ["Wartortle" , "Water"],
    ["Blastoise" , "Water"],
    # Jhoto
    ["Chikorita", "Grass"],
    ["Bayleef", "Grass"],
    ["Meganium", "Grass"],
    ["Cyndaquil" , "Fire"],
    ["Quilava" , "Fire"],
    ["Typhlosion" , "Fire"],
    ["Totodile" , "Water"],
    ["Croconaw" , "Water"],
    ["Feraligatr" , "Water"],
    # Hoenn
    ["Treecko", "Grass"],
    ["Grovyle", "Grass"],
    ["Sceptile", "Grass"],
    ["Torchic", "Fire"],
    ["Combusken", "Fire - Fighting"],
    ["Blaziken", "Fire - Fighting"],
    ["Mudkip", "Water"],
    ["Marshtomp", "Water - Ground"],
    ["Swampert", "Water - Ground"],
    # Sinnoh
    ["Turtwig" , "Grass"],
    ["Grotle" , "Grass"],
    ["Torterra" , "Grass - Ground"],
    ["Chimchar" , "Fire"],
    ["Monferno" , "Fire - Fighting"],
    ["Infernape" , "Fire - Fighting"],
    ["Piplup" , "Water"],
    ["Prinplup" , "Water"],
    ["Empoleon" , "Water - Steel"],
    # Unova
    ["Snivy", "Grass"],
    ["Servine", "Grass"],
    ["Serperior", "Grass"],
    ["Tepig", "Fire"],
    ["Pignite", "Fire - Fighting"],
    ["Emboar", "Fire - Fighting"],
    ["Oshawott", "Water"],
    ["Dewott", "Water"],
    ["Samurott", "Water"],
    # Kalos
    ["Chespin", "Grass"],
    ["Quilladin", "Grass"],
    ["Chesnaught", "Grass - Fighting"],
    ["Fennekin", "Fire"],
    ["Braixen", "Fire"],
    ["Delphox", "Fire - Psychic"],
    ["Froakie", "Water"],
    ["Frogadier", "Water"],
    ["Greninja", "Water - Dark"],
    # Alola
    ["Rowlet" , "Grass - Flying"],
    ["Dartrix" , "Grass - Flying"],
    ["Decidueye" , "Grass - Ghost"],
    ["Litten" , "Fire"],
    ["Torracat" , "Fire"],
    ["Incineroar" , "Fire - Dark"],
    ["Popplio" , "Water"],
    ["Brionne" , "Water"],
    ["Primarina" , "Water - Fairy"]])
print (table)