import microbit as mb
import time

SOIL_MOISTURE_PIN = mb.pin0
PUMP = mb.pin8


def run_pump(wait_time=0):

    mb.display.show(mb.Image.UMBRELLA)

    PUMP.write_digital(1)

    time.sleep(3)

    PUMP.write_digital(0)

    if wait_time:
        time.sleep(wait_time)

    mb.display.clear()


def loop():

    count = 0
    PUMP.write_digital(0)

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

        if count == 0:
            run_pump(60)

        rest_for = 60 if count > 60 else 1

        for _ in range(rest_for):

            if mb.button_a.is_pressed():
                mb.display.scroll(soil_moisture)

            if mb.button_b.is_pressed():
                run_pump()

            time.sleep(1)


loop()
