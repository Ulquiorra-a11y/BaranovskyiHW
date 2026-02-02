import random


task_level = 3
match task_level:
    case 1:
        n = int(input("Введите число: "))
        sum_n = 0
        while n > 0:
            sum_n += n % 10
            n //= 10
            print("Сумма цифр: :", sum_n)
    case 2:
        print("Task 2")
        n = int(input("Введите число: "))
        tmp = n
        i = 0
        while tmp > 0:
            i = i * 10 + tmp % 10
            tmp //= 10
        if n == i:
            print('Число ', n, ' является палиндромом')
        else:
            print('Число ', n, ' не является палиндромом')
    case 3:
        print("Task 3")
        secret_number = random.randint(1, 100)
        attempts = 10
        guess = False


        while attempts > 0:
            n = int(input('Число: '))
            attempts -= 1
            if secret_number == int(n):
                print("Вы выиграли!")
                guess = True
                break
            elif secret_number < int(n):
                print('Загаданное число меньше вашего')
            else:
                print('Загаданное число больше вашего')
                if attempts == 0:
                    print("Иди тренируйся")
        if guess:
            if attempts == 9:
                print("Читер")
            elif attempts >= 6:
                print("Отличная интуиция, но я тебе все равно не доверяю")
            elif attempts >= 3:
                print("Not bad, not bad")
            else:
                print("Еле еле, в казино сегодня не иди")









