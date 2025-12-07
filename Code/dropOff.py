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
MAG_THRESH = 250
DROP_DELAY = 0.2
FIND_DELAY = 2.0
#STRAGHT_TIME = 4
HILL_TOP_TIME = 2
INTEGRATION_WAIT = 2
MAG_TURN_WAIT = 1

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
    destination = 1
    runCondition = 0
    
    try:
        print("Start")
        straightTime = Timer(HILL_TOP_TIME)
        integrationTimer = Timer(INTEGRATION_WAIT)
        magTurnTimer = Timer(MAG_TURN_WAIT)
        runTime = Timer()
        tel = Telemetry(runTime)
        d = Drive(tel)
        pay = Payload(tel, MAG_THRESH)
        
        time.sleep(1)
        
        print("Initialized")
        
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

                match runCondition:
                    case 0: # Removing incline error
                        if integrationTimer.flagReached():
                            case = 0.1
                        else:
                            print("Integration wait")
                            incline = 0
                    case 0.1: # Goinng up hill
                        if incline > INLINE_THRESH:
                            tel.add("Going Up")
                            d.fullSmartStraight(STRAIGHT_SPEED, angle)
                            straightTime.reset()
                        else:
                            runCondition = 1
                            d.fullSmartStraight(STRAIGHT_SPEED, angle)
                            straightTime.reset()
                    case 1: # Top of hill
                        if straightTime.flagReached():
                            runCondition = 2
                        else:
                            tel.add("Going Up - After")
                            d.fullSmartStraight(STRAIGHT_SPEED, angle)
                    case 2: # Line following
                        d.lineFollow(lineFound, STRAIGHT_SPEED, SWEEP_SPEED, angle)
                        if mags >= destination:
                            runCondition = 3:
                            magTurnTimer.reset()
                    case 3: # Going straight
                        d.lineFollow(lineFound, STRAIGHT_SPEED, SWEEP_SPEED, angle)
                        if magTurnTimer.flagReached():
                            runCondition = 4
                    case 4: # Turning right
                        if turnRight(angle, -90, SWEEP_SPEED):
                            case = 5
                    case 5:
                        if mags >= destination + 1:
                            pay.drop(DROP_DELAY)
                        else:
                            d.lineFollow(lineFound, STRAIGHT_SPEED, SWEEP_SPEED, angle)
                        


#                 if integrationTimer.flagReached():
#                     if mags >= destination:
#                         if d.turnRight(angle, -90, SWEEP_SPEED):
#                             d.lineFollow(lineFound, STRAIGHT_SPEED, SWEEP_SPEED, angle)
#                             if mags >= destination + 1:
#                                 pay.drop(DROP_DELAY)
#                     else:
#                         if incline > INLINE_THRESH:
#                             tel.add("Going Up")
#                             d.fullSmartStraight(STRAIGHT_SPEED, angle)
#                             straightTime.reset()
#                         else:
#                             if straightTime.flagReached():
#                                 if lineFound:
#                                     tel.add("Line")
#                                     d.fullSmartStraight(STRAIGHT_SPEED, angle)
#                                 else:
#                                     tel.add("No Line")
#                                     d.sweep(SWEEP_SPEED, angle)
#                             else:
#                                 tel.add("Going Up - After")
#                                 d.fullSmartStraight(STRAIGHT_SPEED, angle)
#                 else:
#                     print("Integration wait")
#                     incline = 0

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