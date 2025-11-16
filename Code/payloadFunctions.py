from basehat import IMUSensor
from buildhat import Motor
from Timer import Timer
import math as m
import time

INITIAL_POS = 90
FINAL_POS = -90

class Payload():

    def __init__(self, telObj, magThresh):
        self.tel = telObj
        self.MAGNET_THRESHOLD = magThresh
        
        self.dropMotor = Motor('D')
        self.dropMotor.run_to_position(INITIAL_POS)
        self.IMU = IMUSensor()
        self.dropping = 0

    def getMagneticStrength(self):
        x, y, z = self.IMU.getMag()
        strength = m.sqrt(x**2 + y**2 + z**2)
        self.tel.add("Mag Strength", strength)
        return strength
    
    def drop(self, delay):
        match self.dropping:
            case 0:
                dropTimer = Timer(delay)
            case 1:
                if dropTimer.flagReached():
                    self.dropMotor.run_to_position(FINAL_POS)
    
    
    def dropPayload(self, openAngle, closeAngle, speed):
        self.dropMotor.run_to_relative_position(openAngle, speed)
        time.sleep(1.5)  
        self.dropMotor.run_to_relative_position(closeAngle, speed)
        
        
    def magReached(self, fieldStrength):
        if fieldStrength > self.MAGNET_THRESHOLD:
            return True
        return False