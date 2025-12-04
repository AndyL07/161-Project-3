import time
from buildhat import Motor
SPEED = 1

def main():
    
    leftMotor = Motor('A')
    rightMotor = Motor('B')

    # Function to print the current speed, position and absolute position of the motors
    def handle_motor(speed, pos, apos):
        """Motor data

        :param speed: Speed of motor
        :param pos: Position of motor
        :param apos: Absolute position of motor
        """
        print("Motor", speed, pos, apos)

    try: 
        while True:
            try:
                leftMotor.pwm(SPEED)
                rightMotor.pwm(SPEED)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")
        leftMotor.stop()
        rightMotor.stop()


if __name__ == '__main__':
    main()