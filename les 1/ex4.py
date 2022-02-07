print("введите число: ")
a = int(input())
ls = []
while a > 10:
    ls.append(a % 10)
    a //= 10
a = max(ls)
print(a)
