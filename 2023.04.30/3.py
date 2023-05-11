list_num1 = input(' Введите целые положительные числа через пробел: ').split()
list_num2 = input(' Введите целые положительные числа через пробел: ').split()
# как следует из задания из каждого ввода формируется отдельный список объектов int.
list_num1 = [int(num) for num in list_num1]
list_num2 = [int(num) for num in list_num2]

if not list_num2:
    print('Да')
elif len(list_num1) >= len(list_num2):
    try:
        if list_num2 == list_num1[list_num1.index(list_num2[0]) : list_num1.index(list_num2[0]) + len(list_num2)]:
            print('Да')
        else:
            print('Нет')
    # если индекс с элементом не найден
    except ValueError:
        print('Нет')
else:
    print('Нет')

# + ещё один способ:
# if str(list_num2).strip('[]') in str(list_num1).strip('[]'):
    # print('Да')
# else:
    # print('Нет')

# третий способ через метод find, он может искать подстроки, а не только одиночные символы. Если подстрока не найден возвращает -1.
# Этот метод всё таки не используем, т.к. в задание найти подсписок, а не подстроку.  
# list_num1 = input(' Введите целые положительные числа через пробел: ')
# list_num2 = input(' Введите целые положительные числа через пробел: ')

# if list_num1.find(list_num2) >= 0:
    # print('Да')
# else:
    # print('Нет')
    
# 1 2 3 4
# 1 2
# Да
   
# 1 2 3 4
# 2 4
# Нет

# проверка если пустая строка
# Введите целые положительные числа через пробел: 1 2 3 4
# Введите целые положительные числа через пробел:
# Да


