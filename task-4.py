your_text = input("Введите предложение из нескольких слов: ").split()
for i, key in enumerate(your_text, 1):
    print(f"{i}) {key[:10]}")
