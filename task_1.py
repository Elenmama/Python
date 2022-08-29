my_list = [2, 5.5, 'tr', (-8+3j), False, None, [8, 2, 5], {8, 2, 5}, (8, 2, 5), {8: 'hello', 9: 'bye'}, b'sometext', bytearray(b'sometext'), ZeroDivisionError, ValueError,frozenset([3,4])]
for index, key in enumerate (my_list,1):
    print(f"{index}){key} - {str(type(key))[8:-2]}")
