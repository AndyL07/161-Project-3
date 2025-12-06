# File Name: <3-4Run.py>
# Date: <11/15/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>


# Imports
# ------------------------------------------
from basehat import LineFinder
from basehat import IMUSensor
from payloadFunctions import Payload
from driveFunctions import Drive
from Telemetry import Telemetry
from Timer import Timer
from Math_Helper import average
import time

# Constants
# ----------------------
WAIT_TIME = 0.05
STRAIGHT_SPEED = 0.6
SWEEP_SPEED = 0.3
INLINE_THRESH = 5
MAG_THRESH = 1000
DROP_DELAY = 0.2
FIND_DELAY = 2.0
STRAGHT_TIME = 4

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
    
    arrGyroY = []
    arrGyroZ = []
    for i in range (100):
        x, y, z = IMU.getGyro()
        arrGyroY.append(y)
        arrGyroZ.append(z)
        time.sleep(0.05)
    
    for i in range(10):
        arrGyroY.pop(0)
        arrGyroZ.pop(0)
    yAvg = average(arrGyroY)
    zAvg = average(arrGyroZ)
    
    newTime = 0
    newGyroZ = 0
    angle = 0
    newGyroY = 0
    incline = 0  
    
    mags = 0
    destination = 2
    destination += 1
    
    straightTime = Timer(2)
    runTime = Timer()
    tel = Telemetry(runTime)
    d = Drive(tel)
    pay = Payload(tel, MAG_THRESH)
    
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
                x, y, z = IMU.getGyro()
                newGyroY = y - yAvg
                newGyroZ = z - zAvg
                
                angle += (newTime - oldTime) * (oldGyroZ + newGyroZ) / 2
                tel.add(angle, "Angle")
                
                incline += (newTime - oldTime) * (oldGyroY + newGyroY) / 2
                tel.add(incline, "Incline")
                
                mags += pay.magFinder(MAG_THRESH, FIND_DELAY)
                tel.add(mags, "Mags Found")

#                 if mags >= destination:
#                     pay.drop(DROP_DELAY)
#                 else:
#                     if incline > INLINE_THRESH:
#                         tel.add("Going Up")
#                         d.fullSmartStraight(STRAIGHT_SPEED, angle)
#                         straightTime.reset()
#                     else:
#                         if straightTime.flagReached():
#                             if lineFound:
#                                 tel.add("Line")
#                                 d.fullSmartStraight(STRAIGHT_SPEED, angle)
#                             else:
#                                 tel.add("No Line")
#                                 d.sweep(SWEEP_SPEED, angle)
#                         else:
#                             tel.add("Going Up - After")
#                             d.fullSmartStraight(STRAIGHT_SPEED, angle)

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