import time

#min första oändliga while-loop
i = 0
avbryt = 'b'
while True:
    if avbryt != 'avbryt':
        print(f'hej {i}')
        time.sleep(0.5)
        avbryt = input('ge kommando :')
        i += 1
    else:
        break

print('slut')
