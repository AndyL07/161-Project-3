import payloadFunctions
import driveFunctions

def main():
    goStraight(50)
    time.sleep(3)

    goGeneralBack(50)
    time.sleep(3)
    
    gofast(50)
    time.sleep(3)
    
    stop()
    time.sleep(3)
    
    turnLeft(90, 50)
    time.sleep(3)

    turnRight(90, 50)
    time.sleep(3)

if __name__ == "__main__":
    main()
