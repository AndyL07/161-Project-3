# File Name: <Base Decision.py>
# Date: <10/20/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>


# Imports
# --------------------------
import time
import grovepi



# Constants/Ports
# --------------------------
# Bases Alpha, Beta, and Gamma are numbers 1, 2, and 3 respectively
LOCATION_NUM = 1

# Connect the Grove Line Finder to digital port D7
# SIG,NC,VCC,GND
line_finder = 7
grovepi.pinMode(line_finder,"INPUT")

# Variable initialization
mags_found = 0
start_t = time.perf_counter()



# Running Code
while True:
    curr_t =time.perf_counter()
    
    line_val = grovepi.digitalRead(line_finder)
    
    
    try:
        # Code to follow line
        # Return HIGH when black line is detected, and LOW when white line is detected
        if line_val == 1:
            print ("black line detected")
            mags_found += 1
            found_t = time.perf_counter()
            
            if mags_found == LOCATION_NUM:
                # Code to turn left
                
                if line_val == 1:
                    
        else:
            print ("white line detected")

        time.sleep(.5)

    except IOError:
        print ("Error")