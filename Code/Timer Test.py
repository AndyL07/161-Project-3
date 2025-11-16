import time
from Timer import Timer

i = 10
runTime = Timer(3)

while i > 0:
    print("---------------------------------")
    print(i)
    print(runTime.currTime())
    print(runTime.getFlag())
    print(runTime.flagReached())
    time.sleep(1)
    i -= 1
    if i <= 5:
        runTime.setFlag(7)