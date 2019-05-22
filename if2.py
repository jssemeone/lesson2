def compare(line1, line2):
    
    if len(line1) == len(line2):
        return 1

    # elif len(line1) > len(line2):
    #     return 2

    # elif len(line1) != len(line2):

    #     if line2 == "learn":
    #         return 3

    # variant = isinstance(line1, line2, str)

    # if variant == True:
    #     return 0

line1 = input("Введите первое слово - ")

line2 = input("Введите второе слово - ")

result = compare

print(result)