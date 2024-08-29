f = open('my_numbers.txt', mode='r')

acc = 0
for rad in f:
    acc += int(rad)
    print(acc)



f.close()