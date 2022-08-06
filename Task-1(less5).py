with open('file1.txt', 'w', encoding='utf-8') as f:
    while True:
        my_line = input('введите строку или пустую строку: ')
        if not my_line:
            break
        print(my_line, file=f)
