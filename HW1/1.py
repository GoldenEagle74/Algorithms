# Пускаем число в цикл пока оно не станет равно нулю
# Если число четное, то делим пополам
# Иначе отнимаем единицу
# В конце каждой операции увеличиваем счетчик

# Сложность Q(n)


def numberOfSteps(num):
    cnt = 0
    while num != 0:
        if num % 2: num -= 1
        else: num //= 2
        cnt += 1
    return cnt

print(numberOfSteps(int(input())))
