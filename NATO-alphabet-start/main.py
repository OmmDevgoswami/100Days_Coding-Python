import pandas
data = pandas.read_csv("NATO-alphabet-start\\nato_phonetic_alphabet.csv")
nato_phonetic = {row.letter:row.code for (index,row) in data.iterrows()}
word = input("Enter the Word: ").upper()
word_list = [letter for letter in word]

NATO_expression = [nato_phonetic[NATO] if NATO in nato_phonetic.keys() else NATO for NATO in word_list ]
print (NATO_expression)