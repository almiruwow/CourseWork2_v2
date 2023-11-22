from player import Player
from utils import load_random_word


def main():
    user_name = input('Введите свое имя: ')
    test = load_random_word(user_name)
    class_instance = Player(user_name)
    print(test)

    while class_instance.sheck_word() != len(test.sub_word):
        user_input = input().lower().strip()
        if user_input in ['stop', 'стоп']:
            print(f'\nигра завершена!\n'
                  f'Вы угадали {class_instance.sheck_word()} слов')
            break
        elif test.sheck_word(user_input):
            if class_instance.check_words_used(user_input):
                print('Вы уже угадали это слово')
                continue
            class_instance.append(user_input)
            print('Верно')
        else:
            print('Неверно')

    if class_instance.sheck_word() == len(test.sub_word):
        print(f'\nCлова закончились, игра завершена!\n'
              f'Вы угадали {class_instance.sheck_word()} слов')


if __name__ == '__main__':
    main()
