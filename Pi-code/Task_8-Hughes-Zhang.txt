from gpiozero import LED, Button
from time import sleep

# GPIO18 (physical pin 12), GPIO23 (physical pin 16)
led = LED(18)
button = Button(23, pull_up=False)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()
    sleep(0.05)
