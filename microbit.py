# Dummy microbit class to stop pylint complaining


class ImageClass():

    def __init__(self):

        self.HAPPY = None
        self.SAD = None


class PinClass():

    def read_analog(self):
        return 0


class DisplayClass():

    def scroll(self, ignore):
        pass

    def show(self, ignore):
        pass

    def clear(self):
        pass


pin0 = PinClass()
display = DisplayClass()

Image = ImageClass()
