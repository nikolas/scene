import png


class Font():
    def __init__(self):
        filename = 'scene/font8x12.png'
        with open(filename, 'rb') as f:
            r = png.Reader(file=f)
            print(r.read())
