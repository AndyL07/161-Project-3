from basehat import IMUSensor
from buildhat import Motor
import time
import math

# IMU = IMUSensor()         
dropMotor = Motor('B')       
driveMotor = Motor('C')      
steerMotor = Motor('D')  
IMU = IMUSensor()

OPEN_ANGLE = 90            
CLOSE_ANGLE = -90  
MAGNET_THRESHOLD = 300.0
DRIVE_SPEED = -0.6  
STEER_SPEED = 30    
LEFT_ANGLE = 60     
RIGHT_ANGLE = -90   
STRAIGHT_ANGLE = 0  
    

def main():
    try:
        while True:
            try:
                driveMotor.pwm(DRIVE_SPEED)

                if detectAndDrop(dropMotor):
                    pass
                
                time.sleep(0.3)

            except IOError:
                break

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")
       # try:
            #dropMotor.stop()
       # except:
            #pass

def getMagneticStrength():
    x, y, z = IMU.getMag()
    strength = math.sqrt(x**2 + y**2 + z**2)
    return strength

def drop():
    dropMotor.pwm(0.5)

'''
def dropPayload(motor, openAngle, closeAngle, speed):
    dropMotor.run_to_relative_position(openAngle, speed)
    time.sleep(1.5)  
    dropMotor.run_to_relative_position(closeAngle, speed)
    '''
    
def magReached(old_field, new_field):
    if new_field > MAGNET_THRESHOLD:
        if new_field < old_field:
            return True
    return False

def turnLeft(angle):
    steerMotor.run_to_position(angle, direction='shortest', blocking="False")

def turnRight(angle):
    steerMotor.run_to_position(-angle, direction='shortest', blocking="False")
    
def get_angle():
    return steerMotor.get_aposition()

def goStraight():
    steerMotor.run_to_position(0, direction='shortest', blocking="False")
    driveMotor.pwm(DRIVE_SPEED)

def goGeneralForward():
    driveMotor.pwm(DRIVE_SPEED)
    
def goGeneralBack():
    driveMotor.pwm(-1.4 * DRIVE_SPEED)
    
def stop():
    driveMotor.pwm(0)
    steerMotor.pwm(0)
    
def gofast():
    driveMotor.pwm(1)
       

if __name__ == '__main__':
    main()
