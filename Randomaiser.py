import random

while True:
    n = int(input("Введите максимальное число"))
    print(random.randint(1, n))
    again = input("Сгенерировать еще число? д - да, н - нет")
    if again == "н":
        break
print("Спасибо что воспользовались нашим генератором чисел!")
