# File Name: <Cargo Dropoff.py>
# Date: <10/20/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>


# Imports
# --------------------------
import time
import math as m
from basehat import IMUSensor
#from magDetectAndDropPayload import goStraight, stop, turnLeft, turnRight, goGeneralForward, goGeneralBack
from magDetectAndDropPayload import *
from basehat import LineFinder

# Constants
# ----------------------
WAIT_TIME = 0.05
MAX_BREAK_TIME = 4
TURN_TIME = 2
LOW_TURN = 35
HIGH_TURN = 60

# Running Code
# ------------------------
def main():
    # set the pin to be used
    # if sensor is plugged into port D5, pin1 should be 5
    # make sure to only plug in LineFinder Sensor to digital ports of the Grove BaseHAT (D5, D16, D18, D22, D24, D26)
    # rlf_pin = 5
    # llf_pin = 22

    # Initializing the sensor so the function within the class can be used
    # r_line_find = LineFinder(rlf_pin)
    # l_line_find = LineFinder(llf_pin)
    IMU = IMUSensor()
    
    # line = True    
    total_mag = 0
    
    # Start Time
    start_time = time.perf_counter()
    
    try: 
        while True:
            try: 
                # Get magnetic field
                last_mag = total_mag
                total_mag = getMagneticStrength()

                if magReached(last_mag, total_mag):
                    print("Dropping off...")
                    

                # Tellemetry
                print("------------------------------------------")
                #print(" MX = %7.2f uT \t MY = %7.2f uT \t MZ = %7.2f uT" % (x, y, z))
                print("Mag Strength - %7.2f uT" % total_mag)
                print("Last Mag - %7.2f uT" % last_mag)
                print("------------------------------------------")

                # Wait time
                time.sleep(WAIT_TIME)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break

    except KeyboardInterrupt:
        goStraight()
        time.sleep(WAIT_TIME)
        stop()
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()
    
# def curr_time():
#     return time.perf_counter() - start_time`