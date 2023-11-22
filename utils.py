from random import choice
from basicword import BasicWord
from json_decode import my_list

my_list = my_list


def load_random_word(user_name):
    my_new_list = choice(my_list)

    class_instance = BasicWord(my_new_list['word'], my_new_list['subwords'], user_name)

    return class_instance


