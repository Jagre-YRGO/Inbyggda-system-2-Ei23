def my_func(listan):
    listan[0] = 50
    return listan

input_lista = [1,2,3,4,5]
print('reversed list:' + str(my_func(input_lista.copy())))
print(f'reversed list: {my_func(input_lista.copy())}')
print(input_lista)
