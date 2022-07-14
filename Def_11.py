def print_goods(*args):
    count=0
    for i in args:
        if isinstance(i,str):
            if len(i)>0:
                count+=1
                print(f'{count}. {i}')
    if count==0:
        print('Нет товаров')
