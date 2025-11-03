def getMagneticStrength():
    x, y, z = IMU.getMag()
    strength = math.sqrt(x**2 + y**2 + z**2)
    return strength

def drop():
    dropMotor.pwm(0.5)


def dropPayload(motor, openAngle, closeAngle, speed):
    dropMotor.run_to_relative_position(openAngle, speed)
    time.sleep(1.5)  
    dropMotor.run_to_relative_position(closeAngle, speed)
    
    
def magReached(old_field, new_field):
    if new_field > MAGNET_THRESHOLD:
        if new_field < old_field:
            return True
    return False