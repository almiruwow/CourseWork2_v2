class Player:

    def __init__(self, user_name):
        self.user_name = user_name
        self.words_used = []

    def sheck_word(self):
        return len(self.words_used)

    def append(self, word):
        self.words_used.append(word)

    def check_words_used(self, word):
        return word in self.words_used


