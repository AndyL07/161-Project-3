from buildhat import Motor
from Telemetry import Telemetry
import time

class Drive:
    def __init__(self, telObj):
        self.tel = telObj
        
        self.leftMotor = Motor('A')
        self.rightMotor = Motor('B')

    def turnLeft(self, angle, power):
        self.leftMotor.stop()
        self.rightMotor.run_for_degrees(angle, speed=power, blocking=False)
        self.tel.add("Turning Left")
        print(self.tel)
        self.tel.reset()

    def turnRight(self, angle, power):
        self.rightMotor.stop()
        self.leftMotor.run_for_degrees(angle, speed=-power, blocking=False)
        self.tel.add("Turning Right")
        print(self.tel)
        self.tel.reset()
        

    def goStraight(self, speed):
        self.leftMotor.pwm(-speed)
        self.rightMotor.pwm(speed)
        self.tel.add("Going Straight")
        print(self.tel)
        self.tel.reset()
        
    def goGeneralBack(self, speed):
        self.leftMotor.pwm(1.4 * speed)
        self.rightMotor.pwm(-1.4 * speed)
        self.tel.add("Going Back")
        print(self.tel)
        self.tel.reset()
        
    def stop(self):
        self.leftMotor.pwm(0)
        self.rightMotor.pwm(0)
        self.tel.add("Stopping")
        print(self.tel)
        self.tel.reset()
        
    def gofast(self, speed):
        self.leftMotor.pwm(2 * speed)
        self.rightMotor.pwm(2 * speed)
        self.tel.add("Going Fast")
        print(self.tel)
        self.tel.reset()
    
