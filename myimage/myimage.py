from PIL import Image

class MyImage:
    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(filename)
        self.width, self.height = self.image.size

    def getPixel(self, x, y):
        return self.image.getpixel((x, y))

    def setPixel(self, pos, rgb):
        self.image.putpixel(pos, rgb)

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def save(self, filename=None):
        if not filename:
            filename = self.filename
        self.image.save(filename)

    def draw(self):
        self.image.show()

    def clone(self):
        return MyImage(self.filename)

