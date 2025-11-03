# IMUSensor_Example.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the basehat folder
# on your Pi's Desktop 

# import the necessary packages for your sensor and code
from basehat import IMUSensor
import time
import pandas as pd
#import matplotlib.pyplot as plt

def main():
    # Constants
    WAIT_TIME = 0.2
    
    # Initializing the IMU so the example can utilize the sensor
    IMU = IMUSensor()
    
    X_accel = []
    Y_accel = []
    Z_accel = []
    
    X_gyro = []
    Y_gyro = []
    Z_gyro = []
    
    X_mag = []
    Y_mag = []
    Z_mag = []   
    
    time_data = []
    
    # Start Time
    start_time = time.perf_counter()
    
    try: 
        while True:
            try:
                # Reading acceleration values and printing them
                x, y, z = IMU.getAccel()
                print(" AX = %7.2f m/s^2 \t AY = %7.2f m/s^2 \t AZ = %7.2f m/s^2" % (x, y, z))
                X_accel.append(x)
                Y_accel.append(y)
                Z_accel.append(z)

                # Reading gyroscope values and printing them
                x, y, z = IMU.getGyro()
                print(" GX = %7.2f dps \t GY = %7.2f dps \t GZ = %7.2f dps" % (x, y, z))    
                X_gyro.append(x)
                Y_gyro.append(y)
                Z_gyro.append(z)

                # Reading magnet values and printing them
                x, y, z = IMU.getMag()
                print(" MX = %7.2f uT \t MY = %7.2f uT \t MZ = %7.2f uT" % (x, y, z))
                X_mag.append(x)
                Y_mag.append(y)
                Z_mag.append(z)

                time_data.append(time.perf_counter() - start_time)

                print("-----------------------------------------------------------------------------")
                # Waiting 1 second until new sensor readings   
                time.sleep(WAIT_TIME)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break
    except KeyboardInterrupt:
        df = pd.DataFrame(
            {
                "X Accel":pd.Series(X_accel),
                "Y Accel":pd.Series(Y_accel),
                "Z Accel":pd.Series(Z_accel),
                
                "X Gyro":pd.Series(X_gyro),
                "Y Gyro":pd.Series(Y_gyro),
                "Z Gyro":pd.Series(Z_gyro),
                
                "X Mag":pd.Series(X_mag),
                "Y Mag":pd.Series(Y_mag),
                "Z Mag":pd.Series(Z_mag),
            }
        )
        df.to_excel("IMUData.xlsx")
        print("\nCtrl+C detected. Exiting...")


if __name__ == '__main__':
    main()