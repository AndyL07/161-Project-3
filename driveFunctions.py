from buildhat import Motor

def __init__(telObj):
    tel = telObj
    
    leftMotor = Motor('A')
    rightMotor = Motor('B')

    def turnLeft(angle, power):
        leftMotor.stop()
        rightMotor.run_for_degrees(angle, speed=power, blocking=False)
        tel.add("Turning Left")
    
    def turnRight(angle, power):
        rightMotor.stop()
        leftMotor.run_for_degrees(angle, speed=power, blocking=False)
        tel.add("Turning Right")
        
    
    def goStraight(speed):
        leftMotor.pwm(speed)
        rightMotor.pwm(speed)
        tel.add("Going Straight")
        
    def goGeneralBack(speed):
        leftMotor.pwm(-1.4 * speed)
        rightMotor.pwm(-1.4 * speed)
        tel.add("Going Back")
        
    def stop():
        leftMotor.pwm(0)
        rightMotor.pwm(0)
        tel.add("Stopping")
        
    def gofast(speed):
        leftMotor.pwm(2 * speed)
        rightMotor.pwm(2 * speed)
        tel.add("Going Straight")