dict_inp = {}

while True:
    dict_pair = input(' Введите ключ и значение через пробел: ').split()
    if not dict_pair:
        break
    dict_inp[dict_pair[0]] = dict_pair[1]

inp_value = input(' Введите значение из словаря: ')

# КОММЕНТАРИЙ: да, ключей, сопоставленных одному значению, может быть и несколько, всё верно
if key := {k for k in dict_inp if dict_inp[k] == inp_value}:
    print(*key)
else:
    print('! value error !')

# ИСПОЛЬЗОВАТЬ: а можно без :=, но с тернарным оператором:
keys = {k for k in dict_inp if dict_inp[k] == inp_value}
print(*keys if keys else '! value error !')


# 123 арбуз
# 124 груша
# 125 слива
# 126 апельсин
# 126 ананас
# 127 манго
# Введите строку из словаря: слива
# 125

# СДЕЛАТЬ: вывод целиком! иначе очень неочевидно, как и что именно вы запускаете — если здесь это ещё более-менее угадывается (и то, возможны варианты), то дальше будет совсем грустно — не усложняйте мне работу без надобности, пожалуйста
# Введите строку из словаря: киви
# ! value error !

# 123 груша
# 124 груша
# 125 манго
# 126 слива
# 127 арбуз
# Введите значение из словаря: груша
# 123 124


# ИТОГ: отлично — 3/3
