"""
DOCSTRING
"""
import numpy
from PIL import Image

if __name__ == '__main__':
    IMAGE = Image.open('images/dot.png')
    IMAGE_ARRAY = numpy.asarray(IMAGE)
    print(IMAGE_ARRAY)
