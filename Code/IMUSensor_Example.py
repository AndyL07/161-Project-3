# IMUSensor_Example.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the basehat folder
# on your Pi's Desktop 

# import the necessary packages for your sensor and code
from basehat import IMUSensor
from Telemetry import Telemetry
from Timer import Timer
from Math_Helper import average
import time

def main():

    # Initializing the IMU so the example can utilize the sensor
    IMU = IMUSensor()
    
    arrAccelY = []
    for i in range(10):
        x, y, z = IMU.getAccel()
        arrAccelY.append(z)
        time.sleep(0.05)
    avgAccelY = average(arrAccelY)
    
    ACCEL_THRESH = 0.075
    
    newTime = 0
    newGyroZ = 0
    angle = 0
    newAccelY = 0
    newVelY = 0
    Ypos = 0
        
    runTime = Timer()
    tel = Telemetry(runTime)
    
    try: 
        while True:
            try:
                # Sets values of previous loop
                oldTime = newTime
                oldGyroZ = newGyroZ
                oldAccelY = newAccelY
                oldVelY = newVelY
                
                newTime = runTime.currTime()
                
                # Reading acceleration values and printing them
                x, y, z = IMU.getAccel()
#                 tel.add(" AX = %7.2f m/s^2 \t AY = %7.2f m/s^2 \t AZ = %7.2f m/s^2" % (x, y, z))
                newAccelY = y - avgAccelY
                tel.add(y, "oldAccelY")
                tel.add(newAccelY, "newAccelY")
                if abs(newAccelY < ACCEL_THRESH):                    
                    newAccelY = 0
                    
                arrAccelY.pop(0)
                arrAccelY.append(y)
                avgAccelY = average(arrAccelY)
                tel.add(avgAccelY, "Average")

                # Reading gyroscope values and printing them
                x, y, z = IMU.getGyro()
                newGyroZ = z
#                 tel.add(" GX = %7.2f dps \t GY = %7.2f dps \t GZ = %7.2f dps" % (x, y, z))  

                # Reading magnet values and printing them
                x, y, z = IMU.getMag()
#                 tel.add(" MX = %7.2f uT \t MY = %7.2f uT \t MZ = %7.2f uT" % (x, y, z))             
                
                # # Waiting 1 second until new sensor readings   
                # time.sleep(1.0)
                
                angle += (newTime - oldTime) * (oldGyroZ + newGyroZ) / 2
#                 tel.add(angle, "Angle")
                
                newVelY += (newTime - oldTime) * (oldAccelY + newAccelY) / 2
                Ypos += (newTime - oldTime) * (oldVelY + newVelY) / 2
                tel.add(Ypos * 100, "Y Pos")
                
                print(tel)
                tel.reset()

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()
