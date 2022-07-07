a=input()
def count_letters(a):
    count_1=0
    count_2=0
    for i in a:
        if i.isupper():
            count_2+=1
        if i.islower():
            count_1+=1
    print(f'Количество заглавных символов: {count_2}')
    print(f'Количество строчных символов: {count_1}')
count_letters(a)
