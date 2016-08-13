import RPi.GPIO as GPIO
import sys
sys.path.insert(0, '/home/pi/sensors/vendor')

from temperature import *

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

print get_temperature_humidity()