with open('file3.txt', 'r', encoding='utf-8') as f:
    salary_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя зарплата = {round(sum(salary_dict.values())/len(salary_dict), 3)}\n'
          f'Работники с зарплатой меньше 20к {[e[0] for e in salary_dict.items() if e[1]<20000]}')
