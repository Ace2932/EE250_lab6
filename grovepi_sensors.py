import sys
import os
_dex = os.path.expanduser('~/Dexter')
for _p in (os.path.join(_dex, 'GrovePi', 'Software', 'Python'),
           os.path.join(_dex, 'GrovePi', 'Script'),
           _dex):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# Rotary angle sensor connected to analog port A1 (output [0, 1023])
rotary_sensor = 1
grovepi.pinMode(rotary_sensor, "INPUT")

# Ultrasonic range observed in testing [0, 517] cm
ULTRASONIC_MAX = 517
ROTARY_MAX = 1023

# Clear LCD screen before starting main loop
setText("")

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    distance = grovepi.ultrasonicRead(ultrasonic_ranger)

    # Read rotary [0, 1023], map to threshold range [0, 517] for comparison with raw ultrasonic
    rotary_value = grovepi.analogRead(rotary_sensor)
    threshold = int(rotary_value * ULTRASONIC_MAX / ROTARY_MAX)

    # Object present when raw ultrasonic output falls below threshold
    object_present = distance < threshold
    # TODO: print the object present status on LCD
    # Top line: current threshold value + space, then " OBJ PRES" if object present
    line1 = f"{threshold} "
    if object_present:
      line1 += " OBJ PRES"
    line1 = (line1 + " " * 16)[:16]
    
    # Bottom line: current raw ultrasonic ranger output
    line2 = (str(distance) + " " * 16)[:16]

    setText_norefresh(line1 + "\n" + line2)

  except IOError:
    print("Error")
  time.sleep(0.1)