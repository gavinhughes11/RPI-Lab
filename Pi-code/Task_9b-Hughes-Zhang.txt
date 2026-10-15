from gpiozero import LED, Button
from time import sleep

led_pins = [18, 23, 24, 25, 12, 16, 20, 21, 26]
leds = [LED(pin) for pin in led_pins]
button = Button(19, pull_up=False)

running = False
current_index = 0

for led in leds:
    led.off()

while True:
    # Check for button press to toggle state
    if button.is_pressed:
        running = not running
        # Turn off all LEDs when stopping
        if not running:
            for led in leds:
                led.off()
        # Wait for button release before continuing
        button.wait_for_release()
        sleep(0.2)

    # When active, cycle through the LEDs
    if running:
        for led in leds:
            led.off()
        leds[current_index].on()

        # Increment index
        current_index = (current_index + 1) % len(leds)

        # Short step with repeated button checks during delay
        for _ in range(30):
            if button.is_pressed:
                break
            sleep(0.01)
    else:
        sleep(0.05)
