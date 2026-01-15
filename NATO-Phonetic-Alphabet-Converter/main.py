import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row["letter"] : row["code"] for (index, row) in df.iterrows()}


word = input("Enter a word: ").upper()
output = [dictionary[letter] for letter in word]
print(output)