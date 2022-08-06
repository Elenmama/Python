with open('file2.txt', 'r', encoding='utf-8') as f_obj:
    instrument=[f'{count}.{line.strip()} - {len(line.split())} слов' for count, line in enumerate(f_obj,1)]
    print(*instrument, f'всего строк - {len(instrument)}.', sep="\n")
