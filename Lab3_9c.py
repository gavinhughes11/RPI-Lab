from gpiozero import LED, Button
from time import sleep

led_pins = [18, 23, 24, 25, 12, 16, 20, 21, 26]
leds = [LED(pin) for pin in led_pins]
button = Button(23, pull_up=False)

# Start with LED 1 ON and all others OFF
for led in leds:
    led.off()

current_index = 0
leds[current_index].on()

while True:
    # Wait until the user presses the button
    button.wait_for_press()

    # Turn off current LED and advance to the next
    leds[current_index].off()
    current_index = (current_index + 1) % len(leds)
    leds[current_index].on()

    # Wait until the user releases the button (debounce)
    button.wait_for_release()
    sleep(0.2)
