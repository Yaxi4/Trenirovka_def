def create_file_with_numbers(n):
    file = open(f'range_{n}.txt', 'a+', encoding='utf-8')
    for i in range(1,n+1):
        file.write(f'{i}\n')
    print(file.read())
create_file_with_numbers(5)