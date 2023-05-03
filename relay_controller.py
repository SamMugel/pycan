import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

relay_channel = 17
GPIO.setup(relay_channel, GPIO.OUT)
GPIO.output(relay_channel, GPIO.LOW)

time.sleep(2)

GPIO.output(relay_channel, GPIO.HIGH)

GPIO.cleanup()
