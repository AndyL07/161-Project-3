import time
from Timer import Timer

i = 10
runTime = Timer(5)

while i > 0:
    print("---------------------------------")
    print(i)
    print(runTime.currTime())
    print(runTime.flagReached())
    time.sleep(1)
    i -= 1