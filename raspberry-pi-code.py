from twilio.rest import Client
import RPi.GPIO as GPIO
import time

# Raspberry Pi Pins Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Twilio Account Setup
account_sid = 'AC74c73ff901fe41d63e0362f72b626798'
auth_token = '4be8c3a8454c8294040514f876ff4c1b'
client = Client(account_sid, auth_token)

# Twilio Function
def twilMsg(channel): 
   print("Received input, sending message now.")
   message = client.messages \
    .create(
         body='Aaishika needs help.',
         from_='+19124612542',
         to='+917827794110'
     )

   print(message.sid)
   GPIO.output(23,GPIO.HIGH)

GPIO.add_event_detect(18, GPIO.FALLING, callback = twilMsg, bouncetime = 2000)

while 1:  
   time.sleep(1)