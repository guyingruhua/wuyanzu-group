nominals = {
    'E6': (
        100, 150, 220, 330, 470, 680
    ),
    'E12': (
        100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820
    ),
    'E24': (
        100, 110, 120, 130, 150, 160, 180, 200, 220, 240, 270, 300, 330, 360, 390, 430, 470, 510, 560, 620, 680, 750, 820, 910
    ),
    'E48': (
        100, 105, 110, 115, 121, 127, 133, 140, 147, 154, 162, 169, 178, 187, 196, 205, 215, 226, 237, 249, 261, 274, 287, 301, 316, 332, 348, 365, 383, 402, 422, 442, 464, 487, 511, 536, 562, 590, 619, 649, 681, 715, 750, 787, 825, 866, 909, 953
    ),
    'E96': (
        100, 102, 105, 107, 110, 113, 115, 118, 121, 124, 127, 130, 133, 137, 140, 143, 147, 150, 154, 158, 162, 165, 169, 174, 178, 182, 187, 191, 196, 200, 205, 210, 215, 221, 226, 232, 237, 243, 249, 255, 261, 267, 274, 280, 287, 294, 301, 309, 316, 324, 332, 340, 348, 357, 365, 374, 383, 392, 402, 412, 422, 432, 442, 453, 464, 475, 487, 499, 511, 523, 536, 549, 562, 576, 590, 604, 619, 634, 649, 665, 681, 698, 715, 732, 750, 768, 787, 806, 825, 845, 866, 887, 909, 931, 953, 976
    )
}


def pick_resistors(resistance: int) -> dict[str, tuple[int]] | None:

    """Возвращает словарь, значения которого являются объектами типа tuple  и содержат ближайшие к переданному номиналы сопротивления из всех рядов сопротивлений.
        Если значение сопротивления вне диапазона от 100 до 999 включительно - возвращает None"""
        
    if 100 < resistance < 999:
    
        dict_result = {}
        
        for key in nominals:
            dict_result[key] = tuple(filter(lambda val: abs(val - resistance) == min(map(lambda val: abs(val- resistance), nominals[key])), nominals[key]))
            
        return dict_result   
        


# >>> print(pick_resistors(1))
# None
# >>> pick_resistors(112)
# {'E6': (100,), 'E12': (120,), 'E24': (110,), 'E48': (110,), 'E96': (113,)}
# >>> pick_resistors(549)
# {'E6': (470,), 'E12': (560,), 'E24': (560,), 'E48': (536, 562), 'E96': (549,)}
# >>> print(pick_resistors(1000))
# None
# >>> print(pick_resistors(120))
# {'E6': (100,), 'E12': (120,), 'E24': (120,), 'E48': (121,), 'E96': (121,)}
# >>>