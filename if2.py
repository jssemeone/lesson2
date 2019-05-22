def compare(line1, line2):
    
    if len(line1) == len(line2):
        return 1

    elif len(line1) > len(line2):
        return 2

    elif len(line1) != len(line2):

        if line2 == "learn":
            return 3

    line1 = isinstance(line1, str)
    line2 = isinstance(line2, str)

    if line1 == True:
        if line2 == True:
            return 0
    

line1 = input("Введите первое слово - ")

line2 = input("Введите второе слово - ")

result = compare(line1, line2)

print(result)