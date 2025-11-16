# File Name: <3-4Run.py>
# Date: <11/15/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>


# Imports
# ------------------------------------------
from basehat import LineFinder
from payloadFunctions import Payload
from driveFunctions import Drive
from Telemetry import Telemetry
from Timer import Timer
import time

# Constants
# ----------------------
WAIT_TIME = 0.05
STRAIGHT_SPEED = 0.8
SWEEP_SPEED = 0.5
MAG_THRESH = 300
DROP_DELAY = 1.2

# Running Code
# ------------------------
def main():
    # set the pin to be used
    # if sensor is plugged into port D5, pin1 should be 5
    # make sure to only plug in LineFinder Sensor to digital ports of the Grove BaseHAT (D5, D16, D18, D22, D24, D26)
    linePin = 5

    # Initializing the sensor so the function within the class can be used
    lineFinder = LineFinder(linePin)
    
    runTime = Timer()
    tel = Telemetry(runTime)
    d = Drive(tel)
    pay = Payload(tel, MAG_THRESH)
    
    d.goStraight(0.8)
    time.sleep(5)
    
    try: 
        while True:
            try: 
                # update and read the values of the lineFinder
                lineFound = lineFinder.value

                if lineFound:
                    print("Line")
                    d.goStraight(STRAIGHT_SPEED)
                else:
                    print("No Line")
                    d.sweep(SWEEP_SPEED)
                    
                mag = pay.getMagneticStrength()
                if mag > MAG_THRESH:
                    pay.drop(DROP_DELAY)

                # Tellemetry
                print(tel)
                tel.reset()

                # Wait time
                time.sleep(WAIT_TIME)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break

    except KeyboardInterrupt:
        d.stop()
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()