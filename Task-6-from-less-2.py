your = int(input("Введите количество наименований товаров: "))
all = []
name = ""
cost = 0
num = 0
ed = ""
for i in range(1, your+1):
    name = input("Введите название товара: ")
    cost = input("Bвeдитe цену товара: ")
    num = int(input("Введите количество товаров: "))
    ed = input("Введите единицу измерения цены товара: ")
    all.append((i, {"название": name, "цена": cost, "количество": num, "ед.": ed}))
output = {"название": [], "цена": [], "количество": [], "ед.": []}

for j in range(your):
    output["название"].append(all[j][1]["название"])
    output["цена"].append(all[j][1]["цена"])
    output["количество"].append(all[j][1]["количество"])
    f = True
    for i in range(len(output["ед."])):
        if all[j][1]["ед."] in output["ед."]:
            f = False
    if f:
        output["ед."].append(all[j][1]["ед."])
print(all, output)
