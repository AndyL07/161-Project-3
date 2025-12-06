#from Advanced_Motor import AdvMotor
from buildhat import Motor
#from Telemetry import Telemetry
from Timer import Timer
#import time

SWEEP_TIME = 0.55
SWEEP_FORWARD_TIME = 0.3
MAX_ANGLE = 30
CORRECTION_COEFF = 1

class Drive:
    def __init__(self, telObj, prints=False):
        self.tel = telObj
        
        self.print = prints
        self.leftMotor = Motor('A')
        self.rightMotor = Motor('B')
        
        self.sweeping = 0
        self.sweepTimer = Timer(SWEEP_TIME)
        self.sweepForwardTimer = Timer(SWEEP_FORWARD_TIME)

    def turnLeft(self, angle, power):
        self.leftMotor.stop()
        self.rightMotor.run_for_degrees(angle, speed=power, blocking=False)
        self.tel.add("Turning Left")
        if self.print:
            print(self.tel)
            self.tel.reset()
            
    def goLeft(self, speed):
        self.leftMotor.pwm(-speed)
        self.rightMotor.pwm(-speed)
        self.tel.add("Going Left")
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
            
    def goRight(self, speed):
        self.leftMotor.pwm(speed)
        self.rightMotor.pwm(speed)
        self.tel.add("Going Right")
        if self.print:
            print(self.tel)
            self.tel.reset()
        
    def goStraight(self, speed, resetCase=True):
        self.leftMotor.pwm(speed)
        self.rightMotor.pwm(-speed)
        self.tel.add("Going Straight")
        if resetCase:
            self.sweeping = 0
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
        
    def sweep(self, speed, angle):
#         self.tel.add(self.sweeping, "Case")
        match self.sweeping:
            case 0:
                self.sweepForwardTimer.reset()
                self.sweepTimer.reset()
                self.sweepTimer.setFlag(SWEEP_TIME)
                self.sweeping = 2
                if angle < 0:
                    self.sweeping = 5
                self.tel.add("Initial Case")
            case 1:
                self.goStraight(speed, False)
                self.tel.add("Sweeping Forward")
#                 self.tel.add(self.sweepForwardTimer.currTime(), "Forward Time")
                
                if self.sweepForwardTimer.flagReached():
                    self.sweepTimer.reset()
                    self.sweepTimer.setFlag(SWEEP_TIME)
                    self.sweeping = 2
            case 2:
                self.goRight(speed)
                self.tel.add("Sweeping Right - 1st")
#                 self.tel.add(self.sweepTimer.getFlag(), "Timer Flag")
                
                if self.sweepTimer.flagReached():
                    self.sweepTimer.reset()
                    self.sweepTimer.setFlag(SWEEP_TIME * 2)
                    self.sweeping = 3
            case 3:
                self.goLeft(speed)
                self.tel.add("Sweeping Left")
#                 self.tel.add(self.sweepTimer.getFlag(), "Timer Flag")
                
                if self.sweepTimer.flagReached():
                    self.sweepTimer.reset()
                    self.sweepTimer.setFlag(SWEEP_TIME)
                    self.sweeping = 4
            case 4:
                self.goRight(speed)
                self.tel.add("Sweeping Right - 2nd")
#                 self.tel.add(self.sweepTimer.getFlag(), "Timer Flag")
                
                if self.sweepTimer.flagReached():
                    self.sweepForwardTimer.reset()
                    self.sweeping = 1
            case 5:
                self.goLeft(speed)
                self.tel.add("Sweeping Left - init")
#                 self.tel.add(self.sweepTimer.getFlag(), "Timer Flag")
                
                if self.sweepTimer.flagReached():
                    self.sweepTimer.reset()
                    self.sweepTimer.setFlag(SWEEP_TIME)
                    self.sweeping = 6
            case 6:
                self.goRight(speed)
                self.tel.add("Sweeping Right - init")
#                 self.tel.add(self.sweepTimer.getFlag(), "Timer Flag")
                
                if self.sweepTimer.flagReached():
                    self.sweepForwardTimer.reset()
                    self.sweeping = 1
                
        if self.print:
            print(self.tel)
            self.tel.reset()
            
    def goSmartStriaght(self, speed, difference, resetCase=True):
        leftSpeed = speed + difference
        rightSpeed = -(speed - difference)
        
        if leftSpeed > 1:
            change = leftSpeed - 1
            rightSpeed += change 
            leftSpeed = 1
        if rightSpeed < -1:
            change = rightSpeed + 1
            leftSpeed += change
            rightSpeed = -1
            
        self.leftMotor.pwm(leftSpeed)
        self.rightMotor.pwm(rightSpeed)
        
        self.tel.add(difference, "Going Smart Straight")
        self.tel.add(abs(rightSpeed), "Right Motor")
        self.tel.add(leftSpeed, "Left Motor")
        if resetCase:
            self.sweeping = 0
        if self.print:
            print(self.tel)
            self.tel.reset()
            
    def fullSmartStraight(self, speed, angle, resetCase=True):
        if (angle % 90 < MAX_ANGLE):
            self.goSmartStriaght(speed, speed * ((angle % 90)/ MAX_ANGLE) * CORRECTION_COEFF, resetCase)
        elif (angle % 90 > (90 - MAX_ANGLE)):
            self.goSmartStriaght(speed, speed * (((angle % 90) - 90) / MAX_ANGLE) * CORRECTION_COEFF, resetCase)
        else:
            self.goStraight(speed)
        
        
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
    
