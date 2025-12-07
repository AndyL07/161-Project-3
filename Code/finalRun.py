# File Name: <finalRun.py>
# Date: <12/6/25>
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
from Math_Helper import average, within
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
ANGLE_THRESH = 20
HILL_DELAY = 2
RELOAD_DELAY = 5

DESTINATION = 2 # PUT 1, 2, OR 3 HERE FOR DROPOFF LOCATION

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
    runCondition = 0
    
    segmentTimer = Timer(2)
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

                match runCondition:
                    case 0: # Start segment
                        d.lineFollow(lineFound, STRAIGHT_SPEED, SWEEP_SPEED, angle)
                        if within(angle, -90, ANGLE_THRESH):
                            runCondition = 1
                    case 1:  # Obstance segmemnt
                        d.fullSmartStraight(STRAIGHT_SPEED, angle)
                        if incline > 6: # Up obstacle incline threshold
                            runCondition = 1.1
                    case 1.1: # Going up obstacle
                        d.fullSmartStraight(STRAIGHT_SPEED, angle)
                        if incline < 3: # Down obstalce incline threshold
                            runCondition = 2
                    case 1.2: # After obstacle
                        d.lineFollow(lineFound, STRAIGHT_SPEED, SWEEP_SPEED, angle)
                        if within(angle, -180, ANGLE_THRESH):
                            runCondition = 2
                    case 2: # Inbetween segment
                        d.lineFollow(lineFound, STRAIGHT_SPEED, SWEEP_SPEED, angle)
                        if within(angle, -90, ANGLE_THRESH):
                            runCondition = 3
                            incline = 0
                    case 3: # Hill segment and fork
                        if incline > INLINE_THRESH:
                            tel.add("Going Up")
                            d.fullSmartStraight(STRAIGHT_SPEED, angle)
                            segmentTimer.setFlag(FIND_DELAY)
                            segmentTimer.reset()
                        else:
                            if segmentTimer.flagReached():
                                tel.add("Flat Again")
                                d.lineFollow(lineFound, STRAIGHT_SPEED, SWEEP_SPEED, angle)
                                if within(angle, -270, ANGLE_THRESH):
                                    runCondition = 4
                            else:
                                tel.add("Going Up - After")
                                d.fullSmartStraight(STRAIGHT_SPEED, angle)
                    case 4: # Magnet Fork
                        if DESTINATION == 3:
                            if mags >= 2:
                                mags = 0
                                runCondition = 5
                            else:
                                d.fullSmartStraight(STRAIGHT_SPEED, angle)
                        if mags >= DESTINATION:
                            if d.turnRight(angle, 90, SWEEP_SPEED):
                                mags = 0
                                runCondition = 5
                        else:
                            d.fullSmartStraight(STRAIGHT_SPEED, angle)
                    case 5: # Dropping cargo
                        if mags > 0:
                            if pay.drop(DROP_DELAY):
                                runCondition = 6
                        else:
                            tel.add(DESTINATION, "Delivering")
                            d.lineFollow(lineFound, STRAIGHT_SPEED, SWEEP_SPEED, angle)
                    case 6: # Following to end
                        d.lineFollow(lineFound, STRAIGHT_SPEED, SWEEP_SPEED, angle)
                        if within(angle, -360, ANGLE_THRESH):
                            runCondition = 7
                            segmentTimer.setFlag(1)
                            segmentTimer.reset()
                    case 7: # End straight
                        if segmentTimer.flagReached():
                            runCondition = 8
                        else:
                            d.lineFollow(lineFound, STRAIGHT_SPEED, SWEEP_SPEED, angle)
                    case 8:
                        if pay.reset():
                            runCondition = 9
                            segmentTimer.setFlag(1)
                            segmentTimer.reset()
                    case 9:
                        if segmentTimer.flagReached():
                            runCondition = 0
                        

                if mags >= DESTINATION:
                    pay.drop(DROP_DELAY)
                else:
                    if incline > INLINE_THRESH:
                        tel.add("Going Up")
                        d.fullSmartStraight(STRAIGHT_SPEED, angle)
                        segmentTimer.reset()
                    else:
                        if segmentTimer.flagReached():
                            d.lineFollow(lineFound, STRAIGHT_SPEED, SWEEP_SPEED, angle)
                        else:
                            tel.add("Going Up - After")
                            d.fullSmartStraight(STRAIGHT_SPEED, angle)

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