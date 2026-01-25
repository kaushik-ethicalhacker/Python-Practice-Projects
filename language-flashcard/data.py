import pandas as pd
import random

class Data:
    def __init__(self):
        try:
            self.df = pd.read_csv("french_words_to_learn.csv")
        except FileNotFoundError:
            self.df = pd.read_csv("french_words.csv")
        self.to_learn = self.df.to_dict(orient="records")
        self.current_card = {}

    def next_word(self):
        if len(self.to_learn) == 0:
            return "Done!"

        self.current_card = random.choice(self.to_learn)
        return self.current_card["French"]

    def word_english(self):
        return self.current_card["English"]


    def save_progress(self):
        self.to_learn.remove(self.current_card)
        data= pd.DataFrame(self.to_learn)
        data.to_csv("french_words_to_learn.csv",index=False)