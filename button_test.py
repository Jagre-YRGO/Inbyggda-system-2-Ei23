from gpiozero import Button

min_knapp = Button(4)

min_knapp.wait_for_press()
print('knapp')
