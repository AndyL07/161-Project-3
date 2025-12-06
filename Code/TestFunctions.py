from payloadFunctions import *
from driveFunctions import Drive
from Data_Collection import DataCollection
from Telemetry import Telemetry
from Timer import Timer
import time

def main():
    runTime = Timer()
    data = DataCollection()
    tel = Telemetry(runTime, data)
    d = Drive(tel, True)
    
#     d.goStraight(.50)
#     time.sleep(3)
# 
#     d.goGeneralBack(.50)
#     time.sleep(3)
#     
#     d.gofast(.50)
#     time.sleep(3)
#     
#     d.stop()
#     time.sleep(3)
#     
#     d.turnLeft(90, 50)
#     time.sleep(3)
# 
#     d.turnRight(90, 50)
#     time.sleep(3)
#     
#     sweepTime = Timer(5)
#     while not sweepTime.flagReached():
#         d.sweep(0.5)

    d.goStraight(0.5)
    time.sleep(3)

    d.goLeft(0.5)
    time.sleep(2)
    
    d.goRight(0.5)
    time.sleep(2)
        
    try: 
        while True:
            try: 
#                 d.sweep(0.5)
                d.goStraight(0.8)

                # Wait time
#                 print(tel)
#                 tel.reset()
                time.sleep(0.05)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break

    except KeyboardInterrupt:
        d.stop()
        print("\nCtrl+C detected. Exiting...")

if __name__ == "__main__":
    main()