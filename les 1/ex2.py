import datetime

sec = print("введите количество секунд: ")
sec = int(input())
result = datetime.timedelta(seconds=sec)
print(result)
