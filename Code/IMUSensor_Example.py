# IMUSensor_Example.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the basehat folder
# on your Pi's Desktop 

# import the necessary packages for your sensor and code
from basehat import IMUSensor
from Telemetry import Telemetry
from driveFunctions import Drive
from Timer import Timer
from Math_Helper import average
import time

def main():

    # Initializing the IMU so the example can utilize the sensor
    IMU = IMUSensor()
    
    arrAccelX = []
    for i in range(10):
        x, y, z = IMU.getAccel()
        arrAccelX.append(x)
        time.sleep(0.05)
    avgAccelX = average(arrAccelX)
    
    arrGyroY = []
    arrGyroZ = []
    for i in range (20):
        x, y, z = IMU.getGyro()
        arrGyroY.append(y)
        arrGyroZ.append(z)
    yAvg = average(arrGyroY)
    zAvg = average(arrGyroZ)
    
    ACCEL_THRESH = 0.0
    SPEED_CHANGER = 0.00001
    TARGET_VEL = 20
    
    newTime = 0
    newGyroZ = 0
    angle = 0
    newGyroY = 0
    incline = 0
    
    newAccelX = 0
    newVelX = 0
    Xpos = 0
        
    runTime = Timer()
    tel = Telemetry(runTime)
    d = Drive(tel)
    
    try:
        driveTime = Timer(20)
        speedTime = Timer(2)
        
        while True:
            try:
                # Sets values of previous loop
                oldTime = newTime
                oldGyroZ = newGyroZ
                oldGyroY = newGyroY
                oldAccelX = newAccelX
                oldVelX = newVelX
                
                newTime = runTime.currTime()
                
                # Reading acceleration values and printing them
                x, y, z = IMU.getAccel()
#                 tel.add(" AX = %7.2f m/s^2 \t AY = %7.2f m/s^2 \t AZ = %7.2f m/s^2" % (x, y, z))
                newAccelX = x - avgAccelX
#                 tel.add(x, "oldAccelX")
#                 tel.add(newAccelX, "newAccelX")
                if abs(newAccelX < ACCEL_THRESH):                    
                    newAccelX = 0
                    
                arrAccelX.pop(0)
                arrAccelX.append(y)
                avgAccelX = average(arrAccelX)
#                 tel.add(avgAccelX, "Average")

                # Reading gyroscope values and printing them
                x, y, z = IMU.getGyro()
                newGyroZ = z - zAvg
                newGyroY = y - yAvg
#                 tel.add(" GX = %7.2f dps \t GY = %7.2f dps \t GZ = %7.2f dps" % (x, y, z))  

                # Reading magnet values and printing them
                x, y, z = IMU.getMag()
                tel.add(" MX = %7.2f uT \t MY = %7.2f uT \t MZ = %7.2f uT" % (x, y, z))             
                
                # # Waiting 1 second until new sensor readings   
                # time.sleep(1.0)
                
                angle += (newTime - oldTime) * (oldGyroZ + newGyroZ) / 2
                tel.add(angle, "Angle")
                
                incline += (newTime - oldTime) * (oldGyroY + newGyroY) / 2
                tel.add(incline, "Incline")
                
                newVelX += (newTime - oldTime) * (oldAccelX + newAccelX) / 2
                Xpos += (newTime - oldTime) * (oldVelX + newVelX) / 2
#                 tel.add(newVelX * 100, "X Vel")
                
#                 if speedTime.flagReached():
#                     speed += (TARGET_VEL - (newVelX * 100)) * SPEED_CHANGER
#                     if speed > 1:
#                         speed = 1
#                     tel.add(speed, "Speed")
#                 else:
#                     speed = 0.3
#                 
#                 if driveTime.flagReached():
#                     tel.add("Stopping")
#                     d.stop()
#                 else:
#                     tel.add("Driving")
#                     d.fullSmartStraight(speed, angle)
                
                print(tel)
                tel.reset()

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()
