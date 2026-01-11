import random 

def is_valid_num(n):
    if 1 <= n <= 100:
        return True
    else:
        return False

num = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку!")
tries = 0

while True:
    print("Введите число от 1 до 100:", end=" ")
    users_num = int(input())

    if not is_valid_num(users_num):
        print("Число должно быть от 1 до 100. Попробуйте еще раз.")
    elif users_num < num:
        print("Ваше число меньше загаданного, попробуйте еще разок.")
        tries += 1
    elif users_num > num:
        print("Ваше число больше загаданного, попробуйте еще разок.")
        tries += 1
    else:
        print("Вы угадали, поздравляем!")
        print("Количество сделанных вами попыток:", tries)

        print("Желаете сыграть еще раз? (да/нет):", end='\n')
        answ = input()
        if answ == "да" or answ == "Да" or answ == "ДА":
            continue
        elif answ == "нет" or answ == "Нет" or answ == "НЕТ":
            print("Спасибо за игру! До свидания!")
            break
        else:
            print('Введите "да" иил "нет"')
        break
 