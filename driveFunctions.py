def turnLeft(angle, power):
    leftMotor.stop()
    rightMotor.run_for_degrees(angle, speed=power, blocking=False)

def turnRight(angle, power):
    rightMotor.stop()
    leftMotor.run_for_degrees(angle, speed=power, blocking=False)
    

def goStraight(speed):
    leftMotor.pwm(speed)
    rightMotor.pwm(speed)
    
def goGeneralBack(speed):
    leftMotor.pwm(-1.4 * speed)
    rightMotor.pwm(-1.4 * speed)
    
def stop():
    leftMotor.pwm(0)
    rightMotor.pwm(0)
    
def gofast(speed):
    leftMotor.pwm(2 * speed)
    rightMotor.pwm(2 * speed)