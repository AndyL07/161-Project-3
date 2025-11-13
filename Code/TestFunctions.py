from payloadFunctions import *
from driveFunctions import Drive
from Telemetry import Telemetry
from Timer import Timer
import time

def main():
    runTime = Timer()
    tel = Telemetry(runTime)
    d = Drive(tel)
    
    d.goStraight(.50)
    time.sleep(3)

    d.goGeneralBack(.50)
    time.sleep(3)
    
    d.gofast(.50)
    time.sleep(3)
    
    d.stop()
    time.sleep(3)
    
    d.turnLeft(90, 50)
    time.sleep(3)

    d.turnRight(90, 50)
    time.sleep(3)
    
    sweepTime = Timer(5)
    while not sweepTime.flagReached():
        d.sweep(0.5)

if __name__ == "__main__":
    main()