from Telemetry import Telemetry

i = 10

while i > 0:
    Telemetry()
    tel = Telemetry()
    tel.add(i, "i")
    tel.add("Testing")
    i -= 1
    print(tel)