# File Name: <New_Run.py>
# Date: <11/13/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>


# Imports
# --------------------------
from basehat import LineFinder
# from payloadFunctions import Payload
from basehat import IMUSensor
from driveFunctions import Drive
from Telemetry import Telemetry
from Timer import Timer
import time

# Constants
# ----------------------
WAIT_TIME = 0.05
STRAIGHT_SPEED = 0.4
SWEEP_SPEED = 0.3
INLINE_THRESH = 10

# Running Code
# ------------------------
def main():
    # set the pin to be used
    # if sensor is plugged into port D5, pin1 should be 5
    # make sure to only plug in LineFinder Sensor to digital ports of the Grove BaseHAT (D5, D16, D18, D22, D24, D26)
    linePin = 5

    # Initializing the sensor so the function within the class can be used
    lineFinder = LineFinder(linePin)
    
    # Initializing the IMU so the example can utilize the sensor
    IMU = IMUSensor()
    
    newTime = 0
    newGyroZ = 0
    angle = 0
    newGyroY = 0
    incline = 0    
    
    runTime = Timer()
    tel = Telemetry(runTime)
    d = Drive(tel)   
    
    try: 
        while True:
            try: 
                # update and read the values of the lineFinder
                lineFound = lineFinder.value
                
                # Sets values of previous loop
                oldTime = newTime
                oldGyroZ = newGyroZ
                oldGyroY = newGyroY
                
                newTime = runTime.currTime()
                x, newGyroY, newGyroZ = IMU.getGyro()
                
                angle += (newTime - oldTime) * (oldGyroZ + newGyroZ) / 2
                tel.add(angle, "Angle")
                
                incline += (newTime - oldTime) * (oldGyroY + newGyroY) / 2
                tel.add(incline, "Incline")

                if incline > INLINE_THRESH:
                    tel.add("Going Up")
                    d.fullSmartStraight(STRAIGHT_SPEED, angle)
                else:
                    if lineFound:
                        tel.add("Line")
                        d.fullSmartStraight(STRAIGHT_SPEED, angle)
                    else:
                        tel.add("No Line")
                        d.sweep(SWEEP_SPEED)

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