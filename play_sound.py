from playsound import playsound
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
while True:
    if not GPIO.input(21):
        playsound('/home/liams/Downloads/morselong.mp3')