print("количество км в 1 день вы бегаете: ")
print("количество км которое надо достичь  за 1 день: ")
x = int(input())
y = int(input())
day = 1
while y - x >= 0:
    x = x + (x * 0.1)
    day += 1
print(day)

