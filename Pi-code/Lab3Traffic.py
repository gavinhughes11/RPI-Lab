from gpiozero import LED
from time import sleep

green_1 = LED(25) # 22
blue_1 = LED(16) # 36
yellow_1 = LED(20) # 38
red_1 = LED(21) # 40

green_2 = LED(5) # 29
blue_2 = LED(6) # 31
yellow_2 = LED(13) # 33
red_2 = LED(19) # 35

on = True

while(on):
    # Side 1 green and pedestrian
    red_1.off()
    green_1.on()
    blue_1.on()
    red_2.on()
    sleep(3)
    # Side 1 just green
    blue_1.off()
    sleep(4)
    # Side 1 yellow
    yellow_1.on()
    green_1.off()
    sleep(1.5)
    yellow_1.off()
    sleep(0.2)
    yellow_1.on()
    sleep(1.3)
    # Both sides red
    red_1.on()
    yellow_1.off()
    sleep(1)
    # Side 2 green and pedestrian
    red_2.off()
    green_2.on()
    blue_2.on()
    sleep(3)
    # Side 2 just green
    blue_2.off()
    sleep(4)
    # Side 2 yellow
    green_2.off()
    yellow_2.on()
    sleep(1.5)
    yellow_2.off()
    sleep(0.2)
    yellow_2.on()
    sleep(1.3)
    # Both sides red
    yellow_2.off()
    red_2.on()
    sleep(1)
