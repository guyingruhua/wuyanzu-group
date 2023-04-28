num_1 = input('Введите первое число: ')
num_2 = input('Введите второе число: ')

if num_1.isdecimal() and num_2.isdecimal():
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_2 == 0:
        print('Ошибка, на ноль делить нельзя')
    # ОТВЕТИТЬ: хорошо, что сделали зависимой друг от друга (а не двумя разными if) проверку этих двух логических выражений выше и ниже — понимаете, почему хорошо?
    # Если второе число будет = 0 код ниже не должен выполняться,иначе программа остановится с ошибкой. 
    # Если бы сделала проверку двумя if, тогда программа проверила бы что число равно 0, выполнит действие print, и перейдёт к коду ниже, и здесь уже произойдет исключительная ситуация.  
    else:         
        # СДЕЛАТЬ: подумайте и перепишите нижеследующую часть кода так, чтобы обойтись только одним блоком elif
        # КОММЕНТАРИЙ: скобки не нужны, их можно опустить
        # remainder_modulo = num_1 % num_2  вместо этого используем моржовый оператор
        add1, add2, add3 = '','',''
        
        if remainder_modulo := num_1 % num_2:
            add1, add2, add3 = 'не ', 'неполное ', f'остаток: {remainder_modulo}'
           
        print(f'{num_1} {add1}делится на {num_2} нацело\n'
              f'{add2}частное: {num_1 // num_2}\n'
              f'{add3}')
else:
    print('Ошибка, некорректный ввод')


# КОММЕНТАРИЙ: что касается учебных задач, то обычно мы подразумеваем, что условный пользователь будет вводить требуемые данные всегда корректно — поэтому проверки на корректность вводимых данных можно не выполнять, пока в задании явным образом не сказано обратное


# Введите первое число: 25
# Введите второе число: 3
# 25 не делится на 3 нацело
# неполное частное: 8
# остаток: 1

# Введите первое число: 8
# Введите второе число: 2
# 8 делится на 2 нацело
# частное: 4

# Введите первое число: 2
# Введите второе число: 0
# Ошибка, на ноль делить нельзя


# ИТОГ: хорошо — 2/3
