import microbit as mb
import time

SOIL_MOISTURE_PIN = mb.pin0


def loop():

    count = 0

    while True:

        soil_moisture = SOIL_MOISTURE_PIN.read_analog()

        if soil_moisture > 700:
            count += 1
        else:
            count = 0

        if count > 0 and count < 60:
            mb.display.show(mb.Image.HAPPY)
        elif count > 60:
            mb.display.clear()
        elif count == 0:
            mb.display.show(mb.Image.SAD)

        rest_for = 60 if count > 60 else 1

        time.sleep(rest_for)


loop()
