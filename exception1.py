# """
# Домашнее задание №1
# Исключения: KeyboardInterrupt
# * Перепишите функцию ask_user() из задания while2, чтобы она 
#   перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
#   и завершала работу при помощи оператора break
    
# """

user_dict = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Программирую'}
def ask_user():
    try:
        while True:
            user_input = input('Задай вопрос - ')
            if user_input in user_dict:
                print(user_dict[user_input])
                break
        
            
    except KeyboardInterrupt:
        print('\nПока')
        


if __name__ == "__main__":
    ask_user()