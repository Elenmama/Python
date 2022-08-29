q = [7, 5, 5, 4, 1]

entering_number = ""
while entering_number !="a":
    i=0
    entering_number = input("Введите новый элемент рейтинга. \nTo exit - q\n")

    if entering_number.isdigit():
        for l in q:
            if int(entering_number)<=l:
                i+=1
            else:
                break
        q.insert(i, float(entering_number))
    print(q)
