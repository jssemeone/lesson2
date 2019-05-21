
age = int(input('Введите ваш возраст - '))

def old(age):
    if age > 100:
        return 'Не верю'
    elif age >= 24:
        return 'Жизнь - боль'
    elif age >= 18:
        return 'Все впереди(нет)'
    elif age >= 7:
        return 'Добро пожаловать'
    elif age < 7:
        return 'Дет. сад, дружище'
cool = old
print(cool)