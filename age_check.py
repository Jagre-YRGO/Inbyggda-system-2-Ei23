#age check - kollar om 20 eller yngre
# avslutar med q

while True:
    my_input = input('ange ålder: ')
    if my_input == 'q':
        break
    if int(my_input) >= 20:
        print('välkommen!')
    else:
        print('hem med dig!')


