import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def twilMsg(channel): 
   print("Button pressed, send message now.")

GPIO.add_event_detect(18, GPIO.FALLING, callback = twilMsg, bouncetime = 2000)

while 1:  
   time.sleep(1)