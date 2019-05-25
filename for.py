# Домашнее задание №1
# Цикл for: Оценки
# * Создать список из словарей с оценками учеников разных классов 
#   школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# * Посчитать и вывести средний балл по всей школе.
# * Посчитать и вывести средний балл по каждому классу.
# """

school=[{"school_class": '4a','scores': [4,5,3,2,1]},
 {"school_class": '4b', 'scores': [5,3,2,2,3]},
  {"school_class": '4c', 'scores': [5,5,1,4,3]}]

def mid (school):
    sum_all_scores = 0
    quant_all_scores = 0
    for summ  in school:
        class_average = sum(summ['scores']) / len(summ['scores'])
        print('среднее значение оценок {} {}'.format(summ['school_class'], class_average))
        sum_all_scores = sum_all_scores + sum(summ['scores'])
        quant_all_scores = quant_all_scores + len(summ['scores'])
    school_average = sum_all_scores / quant_all_scores
    print('Среднее значение ошибок по школе {}'.format(school_average))
    

    

def main():
    mid(school)


if __name__ == "__main__":
    main()