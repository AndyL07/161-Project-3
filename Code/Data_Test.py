# File Name: <Data_Test.py>
# Date: <11/14/25>
# By: <Andrew Lullo>
# <lullo>
# Section: <4>
# Team: <59>

from Data_Collection import DataCollection
from Telemetry import Telemetry
from Timer import Timer
from basehat import IMUSensor

runTime = Timer()
data = DataCollection()
tel = Telemetry(runTime, data)

IMU = IMUSensor()

def main():
    count = 0
    
    try:
        while True:
            try:
                xA, yA, zA = IMU.getAccel()
                tel.addAccel(xA, yA, zA)
                
                xG, yG, zG = IMU.getGyro()
                tel.addGyro(xG, yG, zG)
                
                xM, yM, zM = IMU.getMag()
                tel.addMag(xM, yM, zM)
                
#                 tel.add("Found", "Line", True)
                
                count += 1
                tel.add(count, "Index")
                
                print(tel)
                tel.reset()
            
            except IOError:
                print ("\nError occurred while attempting to read values.")
                break
            
    except KeyboardInterrupt:
        data.toExcel()
        print("\nCtrl+C detected. Exiting...")

if __name__ == "__main__":
    main()