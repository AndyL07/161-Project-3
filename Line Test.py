# File Name: <Line Test.py>
# Date: <10/20/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>


# Imports
# --------------------------
import time
import pandas as pd
from magDetectAndDropPayload import goStraight, stop, turnLeft, turnRight, goStraightBack, goGeneralBack
from basehat import LineFinder

# Constants
# ----------------------
WAIT_TIME = 0.05
MAX_BREAK_TIME = 5

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
    
    line = True    
    
    counter = 0
    count = []
    start_list = []
    end_list = []
    type_list = []
    
    # Start Time
    start_time = time.perf_counter()
    
    try: 
        while True:
            try: 
                counter += 1
                count.append(counter)
                
                action_start_time = time.perf_counter() - start_time
                print(action_start_time)
                start_list.append(action_start_time)
                
                # update and read the values of the lineFinder
                rlf_val = r_line_find.value
                llf_val = l_line_find.value

                if rlf_val and llf_val:
                    move_type = "Driving forward - Line"
                    print(move_type)
                    goStraight()
                    line = True
                elif not(rlf_val or llf_val):
                    move_type = "Driving forward - No Line"
                    print(move_type)
                    goGeneralBack()
                    if line:
                        line = False
                        break_start_time = time.perf_counter() - start_time
                        forward = True
                    # if time.perf_counter() - start_time - break_start_time > MAX_BREAK_TIME:
                    #     if forward:
                    #         forward = False
                    #         reverse_start_time = curr_time()
                elif rlf_val:
                    move_type = "Turning right"
                    print(move_type)
                    turnRight()
                    line = True
                else:
                    move_type = "Turning left"
                    print(move_type)
                    turnLeft()
                    line = True

                # Tellemetry
                #print("------------------------------------------")
                #print("Right Line Finder value: {}".format(rlf_val))
                #print("Left Line Finder value: {}".format(llf_val))
                #print("------------------------------------------")

                action_end_time = time.perf_counter() - start_time
                print(action_end_time)
                end_list.append(action_end_time)
                
                print("------------------------------------------")

                # Wait time
                time.sleep(WAIT_TIME)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break

    except KeyboardInterrupt:
        df = pd.DataFrame(
            {
                'Counter':pd.Series(count, dtype='float64'),
                "Start Time":pd.Series(start_list, dtype='float64'),
                "End Time":pd.Series(end_list, dtype='float64'),
                "Type":pd.Series(type_list, dtype='str'),
            }
        )
        df.to_excel("TimeData.xlsx")
        #stop()
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()
    
# def curr_time():
#     return time.perf_counter() - start_time