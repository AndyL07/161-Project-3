# File Name: <New_Run.py>
# Date: <11/13/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>


# Imports
# --------------------------
import time
#from magDetectAndDropPayload import goStraight, stop, turnLeft, turnRight, goGeneralForward, goGeneralBack
from driveFunctions import *
from basehat import LineFinder
from payloadFunctions import *
from driveFunctions import Drive
from Telemetry import Telemetry
from Timer import Timer
import time

# Constants
# ----------------------
WAIT_TIME = 0.05
MAX_BREAK_TIME = 4
TURN_TIME = 2
LOW_TURN = 35
HIGH_TURN = 80

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
    
    try: 
        while True:
            try: 
                # update and read the values of the lineFinder
                lineFound = lineFinder.value

                if lineFound:
                    d.goStraight(0.5)
                else:
                    d.sweep(0.5)

                # Tellemetry
                print(tel)

                # Wait time
                time.sleep(WAIT_TIME)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break

    except KeyboardInterrupt:
        # goStraight()
        # time.sleep(WAIT_TIME)
        # stop()
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()
    
# def curr_time():
#     return time.perf_counter() - start_time