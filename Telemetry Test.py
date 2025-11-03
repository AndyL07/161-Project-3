from Telemetry import Telemetry

i = 100

while i > 0:
    tel = Telemetry()
    tel.add("i", i)
    i -= 1
    print(tel)