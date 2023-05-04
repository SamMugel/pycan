import time
import RPi.GPIO as GPIO


class RelayController:
    relay_channel = 17

    def activate(self, interval: float) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay_channel, GPIO.OUT)
        GPIO.output(self.relay_channel, GPIO.LOW)
        time.sleep(interval)
        GPIO.output(self.relay_channel, GPIO.HIGH)
        GPIO.cleanup()
