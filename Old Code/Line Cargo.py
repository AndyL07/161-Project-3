# File Name: <Line Finder.py>
# Date: <10/20/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>


# Imports
# --------------------------
import time
#from magDetectAndDropPayload import goStraight, stop, turnLeft, turnRight, goGeneralForward, goGeneralBack
from magDetectAndDropPayload import *
from basehat import LineFinder

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
    rlf_pin = 5
    llf_pin = 22
    

    # Initializing the sensor so the function within the class can be used
    r_line_find = LineFinder(rlf_pin)
    l_line_find = LineFinder(llf_pin)
    IMU = IMUSensor()
    
    line = True    
    total_mag = 0
    
    # Start Time
    start_time = time.perf_counter()
    
    try: 
        while True:
            try: 
                # update and read the values of the lineFinder
                rlf_val = r_line_find.value
                llf_val = l_line_find.value
                
                last_mag = total_mag
                total_mag = getMagneticStrength()

                if rlf_val and llf_val:
                    goStraight()
                    print("Driving forward - Line")
                    line = True
                elif not(rlf_val or llf_val):
                    if line:
                        line = False
                        break_start_time = time.perf_counter() - start_time
                        forward = True
                    
                    if (time.perf_counter() - start_time - break_start_time > TURN_TIME) and (abs(get_angle()) < 10):
                        if get_angle() > 0:
                            turnLeft(HIGH_TURN)
                            print("Left High Turn")
                        else:
                            turnRight(HIGH_TURN)
                            print("Right High Turn")
                    elif time.perf_counter() - start_time - break_start_time > MAX_BREAK_TIME:
                        # if forward:
                        #     forward = False
                        #     reverse_start_time = curr_time()
                        goGeneralBack()
                        print("Driving General Backward - No Line")
                    else:
                        goGeneralForward()
                        print("Driving General Forward - No Line")
                elif rlf_val:
                    # Turn right
                    turnRight(LOW_TURN)
                    print("Turning right")
                    line = True
                else:
                    # Turn left
                    turnLeft(LOW_TURN)
                    print("Turning left")
                    line = True
                    
                if magReached(last_mag, total_mag):
                    print("Dropping off...")
                    time.sleep(0.4)
                    stop()
                    gofast()
                    

                # Tellemetry
                print("------------------------------------------")
                print("Right Line Finder value: {}".format(rlf_val))
                print("Left Line Finder value: {}".format(llf_val))
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
#     return time.perf_counter() - start_time