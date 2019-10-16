import microbit as mb
import time

SOIL_MOISTURE_PIN = mb.pin0
PUMP = mb.pin8


def run_pump():

    mb.display.show(mb.Image.UMBRELLA)

    PUMP.write_digital(1)

    time.sleep(3)

    PUMP.write_digital(0)

    mb.display.clear()


def loop():

    count = 0
    button_a_presses = 0
    button_b_presses = 0

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

        for _ in range(rest_for):

            if button_a_presses is not mb.button_a.get_presses():
                mb.display.scroll(soil_moisture)
                button_a_presses = mb.button_a.get_presses()

            if button_b_presses is not mb.button_b.get_presses():
                run_pump()
                button_b_presses = mb.button_b.get_presses()

            time.sleep(1)


loop()
