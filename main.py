import random 

def is_valid_num(n):
    if 1 <= n <= 100:
        return True
    else:
        return False

num = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку!")

while True:
    print("Введите число от 1 до 100:", end=" ")
    users_num = int(input())

    if not is_valid_num(users_num):
        print("Число должно быть от 1 до 100. Попробуйте еще раз.")
    elif users_num < num:
        print("Ваше число меньше загаданного, попробуйте еще разок.")
    elif users_num > num:
        print("Ваше число больше загаданного, попробуйте еще разок.")
    else:
        print("Вы угадали, поздравляем!")
        break
 