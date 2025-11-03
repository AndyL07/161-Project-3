from basehat import IMUSensor
from buildhat import Motor
import math as m
import time

def __init__(telObj, magThresh):
    tel = telObj
    MAGNET_THRESHOLD = magThresh
    
    dropMotor = Motor('B')
    IMU = IMUSensor()

    def getMagneticStrength():
        x, y, z = IMU.getMag()
        strength = m.sqrt(x**2 + y**2 + z**2)
        tel.add("Mag Strength", strength)
        return strength
    
    def drop():
        dropMotor.pwm(0.5)
    
    
    def dropPayload(openAngle, closeAngle, speed):
        dropMotor.run_to_relative_position(openAngle, speed)
        time.sleep(1.5)  
        dropMotor.run_to_relative_position(closeAngle, speed)
        
        
    def magReached(old_field, new_field):
        if new_field > MAGNET_THRESHOLD:
            if new_field < old_field:
                return True
        return False