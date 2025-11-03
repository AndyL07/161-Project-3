from Telemetry import Telemetry
import time

i = 10

Telemetry()
tel = Telemetry()

while i > 0:
    tel.reset()
    tel.add(i, "i")
    tel.add("Testing")
    i -= 1
    time.sleep(1)
    print(tel)