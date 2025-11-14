#from Advanced_Motor import AdvMotor
from buildHat import Motor
#from Telemetry import Telemetry
from Timer import Timer
#import time

SWEEP_TIME = 1.0

class Drive:
    def __init__(self, telObj, prints=False):
        self.tel = telObj
        
        self.print = prints
        self.leftMotor = Motor('A')
        self.rightMotor = Motor('B')
        
        self.sweeping = 0
        self.sweepTimer = Timer(SWEEP_TIME)

    def turnLeft(self, angle, power):
        self.leftMotor.stop()
        self.rightMotor.run_for_degrees(angle, speed=power, blocking=False)
        self.tel.add("Turning Left")
        if self.print:
            print(self.tel)
            self.tel.reset()

    def turnRight(self, angle, power):
        self.rightMotor.stop()
        self.leftMotor.run_for_degrees(angle, speed=-power, blocking=False)
        self.tel.add("Turning Right")
        if self.print:
            print(self.tel)
            self.tel.reset()
        
    def goStraight(self, speed):
        self.leftMotor.pwm(-speed)
        self.rightMotor.pwm(speed)
        self.tel.add("Going Straight")
        if self.print:
            print(self.tel)
            self.tel.reset()
        
    def goGeneralBack(self, speed):
        self.leftMotor.pwm(1.4 * speed)
        self.rightMotor.pwm(-1.4 * speed)
        self.tel.add("Going Back")
        if self.print:
            print(self.tel)
            self.tel.reset()
        
    def sweep(self, speed):
        match self.sweeping:
            case 0:
                self.leftMotor.run_for_seconds(0.1, speed * 100, blocking=False)
                self.rightMotor.run_for_seconds(0.1, speed * 100, blocking=True)
                
                self.sweepTimer.reset()
                self.sweeping = 1
                self.tel.add("Sweeping Forward")
            case 1:
                # Turn right
                self.leftMotor.pwm(speed)
                self.rightMotor.pwm(speed)
                self.tel.add("Sweeping Right - 1st")
                
                if self.sweepTimer.flagReached():
                    self.sweepTimer.reset()
                    self.sweepTimer.setFlag(SWEEP_TIME * 2)
                    self.sweeping = 2
            case 2:
                # Turn left
                speed *= -1
                self.leftMotor.pwm(speed)
                self.rightMotor.pwm(speed)
                self.tel.add("Sweeping Left")
                
                if self.sweepTimer.flagReached():
                    self.sweepTimer.reset()
                    self.sweepTimer.setFlag(SWEEP_TIME)
                    self.sweeping = 3
            case 3:
                # Turn right
                self.leftMotor.pwm(speed)
                self.rightMotor.pwm(speed)
                self.tel.add("Sweeping Right - 2nd")
                
                if self.sweepTimer.flagReached():
                    self.sweepTimer.reset()
                    self.sweeping = 2
        if self.print:
            print(self.tel)
            self.tel.reset()
        
    def stop(self):
        self.leftMotor.pwm(0)
        self.rightMotor.pwm(0)
        self.tel.add("Stopping")
        if self.print:
            print(self.tel)
        self.tel.reset()
        
    def gofast(self, speed):
        self.leftMotor.pwm(2 * speed)
        self.rightMotor.pwm(2 * speed)
        self.tel.add("Going Fast")
        if self.print:
            print(self.tel)
            self.tel.reset()
    
