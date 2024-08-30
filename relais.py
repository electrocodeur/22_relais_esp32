from machine import Pin
from time import sleep

relais = Pin(15, Pin.OUT)

while True:
  relais.value(0)
  sleep(10)
  
  relais.value(1)
  sleep(10)
