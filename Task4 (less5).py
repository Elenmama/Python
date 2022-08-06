rus_dict = {"one":"один", "two":"два", "three":"три", "four":"четыре"}

with open("file44.txt", "w", encoding='utf-8') as new_file:
    with open("file4.txt", encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in my_file])
