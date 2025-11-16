from basehat import IMUSensor
from buildhat import Motor
from Timer import Timer
import math as m
import time

INITIAL_POS = 160
FINAL_POS = 0

class Payload():

    def __init__(self, telObj, magThresh):
        self.tel = telObj
        self.MAGNET_THRESHOLD = magThresh
        
        self.dropMotor = Motor('A')
        self.dropMotor.run_to_position(INITIAL_POS)
        self.IMU = IMUSensor()
        self.dropping = 0
        self.mag = 0
        self.dropTimer = Timer()
        self.magTimer = Timer()

    def magFinder(self, threshold, delay):
        match self.mag:
            case 0:
                if self.getMagneticStrength() > threshold:
                    self.magTimer = Timer(delay)
                    self.mag = 1
                    return 1
            case 1:
                if self.magTimer.flagReached():
                    self.mag = 0
        return 0

    def getMagneticStrength(self):
        x, y, z = self.IMU.getMag()
        strength = m.sqrt(x**2 + y**2 + z**2)
        self.tel.add(strength, "Mag Strength")
#         self.tel.add("test")
#         print(f"Mag Strength: {strength:2.3f}")
        return strength
    
    def drop(self, delay):
        match self.dropping:
            case 0:
                self.dropTimer = Timer(delay)
            case 1:
                if self.dropTimer.flagReached():
                    self.dropMotor.run_to_position(FINAL_POS, direction='clockwise')
    
    
    def dropPayload(self, openAngle, closeAngle, speed):
        self.dropMotor.run_to_relative_position(openAngle, speed)
        time.sleep(1.5)  
        self.dropMotor.run_to_relative_position(closeAngle, speed)
        
        
    def magReached(self, fieldStrength):
        if fieldStrength > self.MAGNET_THRESHOLD:
            return True
        return False