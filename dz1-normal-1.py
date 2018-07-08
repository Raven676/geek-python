number = int(input("Введите число больше 0, но меньше 10:"))

while True:
    if 0 < number < 10:
        number = number ** 2
        print(number)
        print('Программа успешнго завершена!')
        break
    else:
        print('Неверно, попробуй еще раз.')
        number = int(input("Введите число больше 0, но меньше 10:"))
        continue
