from Telemetry import Telemetry
import time

i = 3

Telemetry()
tel = Telemetry()

while i > 0:
    tel.reset()
    tel.add(i, "i")
    tel.add("Testing")
    tel.add("Test", "Label")
    i -= 1
    time.sleep(1)
    print(tel)