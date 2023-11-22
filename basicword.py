class BasicWord:

    def __init__(self, word, sub_word, user_name):
        self.word = word
        self.sub_word = sub_word
        self.user_name = user_name

    def sheck_word(self, word):
        return word in self.sub_word

    def len_sub_word(self):
        return len(self.sub_word)

    def __repr__(self):
        return f'\nПривет, {self.user_name}\n' \
               f'Составьте {self.len_sub_word()} слов из слова {self.word.upper()}\n' \
               f'Слова должны быть не короче {len(min(self.sub_word))}\n' \
               f'Поехали, ваше первое слово?\n'
