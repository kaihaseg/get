import RPi.GPIO as ruina
from time import sleep
ruina.setmode(ruina.BCM)
ruina.setup(24, ruina.OUT)
while True:
    ruina.output(24, 1)
    sleep(2)
    ruina.output(24, 0)
    sleep(2)
