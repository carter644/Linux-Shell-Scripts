#import time
from time import sleep
from adafruit_circuitplayground import cp

print ("Hello <Your Name>")
while true: 
  cp.red_led = True 
sleep(0.5)
cp.red_led = false 
sleep(0.5)
