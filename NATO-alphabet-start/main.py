
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas
data = pandas.read_csv("NATO-alphabet-start\\nato_phonetic_alphabet.csv")
nato_phonetic = {row.letter:row.code for (index,row) in data.iterrows()}
word = input("Enter the Word: ").upper()
word_list = [letter for letter in word]

NATO_expression = [nato_phonetic[NATO] if NATO in nato_phonetic.keys() else NATO for NATO in word_list ]
print (NATO_expression)