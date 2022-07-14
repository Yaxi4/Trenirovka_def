def shift_letter(letter, shift):
    'Функция сдвигает символ letter на shift позиций'
    if 96 < ord(letter) + shift< 123:
        return chr(ord(letter) + shift)
    if 123 < ord(letter) + shift< 149:
        return chr(ord(letter) + shift-26)
    if ord(letter) + shift>149:
        return chr(ord(letter) + shift-52)
    if ord(letter) + shift<97:
        return chr(ord(letter) + shift+26)




print(shift_letter('w', -26))
