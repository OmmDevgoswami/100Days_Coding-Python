import pandas
data = pandas.read_csv("NATO-alphabet-start\\nato_phonetic_alphabet.csv")
nato_phonetic = {row.letter:row.code for (index,row) in data.iterrows()}

while(True):
    try:
        word = input("Enter a word: ").upper()
        output_list = [nato_phonetic[NATO] for NATO in word]
    except KeyError as error_message:
        print(f"Invalid Input: {error_message}\nPlease Enter Only Alphabets as Input.")
    else: 
        print(output_list)
        break