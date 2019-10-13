# Dummy microbit class to stop pylint complaining


class ImageClass():

    def __init__(self):

        self.HAPPY = None
        self.SAD = None


class PinClass():

    def read_analog(self):
        return 0

    def write_digital(self, ignore):
        pass


class ButtonClass():

    def is_pressed(self):
        return False

    def get_presses(self):
        return 0


class DisplayClass():

    def scroll(self, ignore):
        pass

    def show(self, ignore):
        pass

    def clear(self):
        pass


button_a = ButtonClass()
button_b = ButtonClass()


display = DisplayClass()

pin0 = PinClass()
pin1 = PinClass()
pin2 = PinClass()
pin3 = PinClass()
pin4 = PinClass()
pin5 = PinClass()
pin6 = PinClass()
pin7 = PinClass()
pin8 = PinClass()
pin9 = PinClass()

Image = ImageClass()
