import time
import board
import neopixel
import RPi.GPIO as GPIO

pixels1 = neopixel.NeoPixel(board.D18, 300, brightness = 0.6)
pir = 8
pit = 7

GPIO.setup(pir, GPIO.IN)
GPIO.setup(pit, GPIO.IN)

print("waiting for sensor to settle")
time.sleep(2)
print("detecting motion")

while True:
    if GPIO.input(pir):
        print("Motion detected")

        x = 0
        while x < 300:
            pixels1[x] = (255, 0, 0)
            #pixels1[x-5] = (0, 250, 0)
            pixels1[x-10] = (255, 255, 255)
            x = x+1

        time.sleep(0.001)
        pixels1.fill((250,250,250))
        time.sleep(4)

        x = 0
        while x < 300:
            pixels1[x] = (0, 100, 200)
            pixels1[x-5] = (0, 250, 0)
            pixels1[x -10] = (0,0,0)
            x = x +1
            
        time.sleep(0.001)

        pixels1.fill((0,0,0))
        time.sleep(0.1)

    if GPIO.input(pit):
        print("Motion detected TOP")
        x = 289
        while x > 0:
            pixels1[x] = (255,0,0)
            #pixels1[x+5] = (0, 250, 0)
            pixels1[x+10] = (255, 255, 255)
            x = x-1
        time.sleep(0.001)
        pixels1.fill((255,255,255))
        time.sleep(4)

        x = 289
        while x > 0:
            pixels1[x] = (0, 100, 200)
            pixels1[x+5] = (0, 250, 0)
            pixels1[x + 10] = (0,0,0)
            x = x -1
            
        time.sleep(0.001)

        pixels1.fill((0,0,0))
        time.sleep(0.1)
