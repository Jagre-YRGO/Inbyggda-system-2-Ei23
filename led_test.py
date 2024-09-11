from time import sleep
from gpiozero import LED

my_red_led = LED(17)

for i in range(1,10):
    my_red_led.on()
    sleep(0.1)
    my_red_led.off()
    sleep(0.2)
