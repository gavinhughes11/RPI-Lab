from gpiozero import LED
from time import sleep

# Define the 9 LED pins in sequence around the circle
led_pins = [18, 23, 24, 25, 12, 16, 20, 21, 26]
leds = [LED(pin) for pin in led_pins]

# Ensure all are initially off
for led in leds:
    led.off()

while True:
    for led in leds:
        led.on()
        sleep(0.3)
        led.off()
