"""
DOCSTRING
"""
import matplotlib.pyplot as pyplot
import numpy
import PIL.Image as Image

if __name__ == '__main__':
    IMAGE = Image.open('images/dotndot.png')
    IMAGE_ARRAY = numpy.asarray(IMAGE)
    print(IMAGE_ARRAY)
    pyplot.imshow(IMAGE_ARRAY)
    pyplot.show()
