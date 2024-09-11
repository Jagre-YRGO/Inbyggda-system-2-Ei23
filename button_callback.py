from gpiozero import Button

def my_func():
    print('knapp')

min_knapp = Button(4)
min_knapp.when_pressed = my_func

while True:
    my_age = input('ange ålder')
    print(f'du är {int(my_age)+1} nästa år')


