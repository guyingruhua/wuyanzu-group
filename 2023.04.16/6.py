cell_1 = input('Введите координаты первой клетки: ')
cell_2 = input('Введите координаты второй клетки: ')

if ('a'<= cell_1[0] <= 'h' and '1' <= cell_1[1] <= '8' and
    'a' <= cell_2[0] <= 'h' and '1' <= cell_2[1] <= '8'):
     if -1 <= ord(cell_1[0]) - ord(cell_2[0]) <= 1 and -1 <= int(cell_1[1]) - int(cell_2[1]) <= 1:
         print('Да')
     else:
         print('Нет')
else:
    print('Ошибка, некорректный ввод')

# Введите координаты первой клетки: g3
# Введите координаты второй клетки: f2
# Да

# Введите координаты первой клетки: c6
# Введите координаты второй клетки: d4
# Нет