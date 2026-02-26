# import sys
# import os
# # Dexter libs: di_i2c must be on path before grovepi (grovepi imports it from Dexter/Scripts/di_i2c)
# _dex = os.environ.get('DEXTER_HOME') or '/home/pi/Dexter' if os.path.isdir('/home/pi/Dexter') else os.path.expanduser('~/Dexter')
# _scripts = os.path.join(_dex, 'Scripts')
# if _scripts not in sys.path:
#     sys.path.insert(0, _scripts)
# if os.path.join(_dex, 'GrovePi', 'Software', 'Python') not in sys.path:
#     sys.path.insert(0, os.path.join(_dex, 'GrovePi', 'Software', 'Python'))
# import time
# import grovepi
# from grove_rgb_lcd import *

import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# Rotary angle sensor connected to analog port A0 (output [0, 1023])
rotary_sensor = 0
grovepi.pinMode(rotary_sensor, "ANALOG")

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

    setText_norefresh(" " + line1 + "cm" + "\n" + line2 + "cm")

  except IOError:
    print("Error")
  time.sleep(0.1)