import RPi.GPIO as GPIO
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

def callback(channel):
    print("flame detected")
    

GPIO.add_event_detect(7, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(7, callback)

while True:
    time.sleep(1)
