from payloadFunctions import *
from driveFunctions import *
from Telemetry import Telemetry
from Timer import Timer

def main():
    runTime = Timer()
    tel = Telemetry()
    
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

if __name__ == "__main__":
    main()