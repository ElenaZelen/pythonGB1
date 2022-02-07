print("введите выручку: ")
print("издержки: ")
a = int(input())
b = int(input())
rent = (a - b) / a

if a > b:
    print("прибыль", a - b, "руб")
    print("рентабельность", "{0:.0%}".format(rent))
    if a > b:
        print("введите количество сотрудников: ")
        с = int(input())
        rent1 = (a - b) / с
        print("прибыль на 1 сотрудника", float('{:.2f}'.format(rent1)), "руб")

if a < b:
    print("убыток", a - b)


