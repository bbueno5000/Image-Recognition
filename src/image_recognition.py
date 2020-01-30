"""
DOCSTRING
"""
import matplotlib.pyplot as pyplot
import numpy
import PIL.Image as Image
import statistics.mean as mean

def threshold(image_array):
    balance_array = []
    new_array = image_array
    for each_row in image_array:
        for each_pixel in each_row:
            average = mean(each_pixel[:3])
            balance_array.append(average)

IMAGE_1 = Image.open('images/numbers/0.1.png')
IMAGE_ARRAY_1 = np.array(IMAGE_1)
IMAGE_2 = Image.open('images/numbers/y0.4.png')
IMAGE_ARRAY_2 = np.array(IMAGE_2)
IMAGE_3 = Image.open('images/numbers/y0.5.png')
IMAGE_ARRAY_3 = np.array(IMAGE_3)
IMAGE_4 = Image.open('images/sentdex.png')
IMAGE_ARRAY_4 = np.array(IMAGE_4)
FIGURE = pyplot.figure()
AXIS_1 = pyplot.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
AXIS_2 = pyplot.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
AXIS_3 = pyplot.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
AXIS_4 = pyplot.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)
AXIS_1.imshow(IMAGE_1)
AXIS_2.imshow(IMAGE_2)
AXIS_3.imshow(IMAGE_3)
AXIS_4.imshow(IMAGE_4)
pyplot.show()

if __name__ == '__main__':
    IMAGE = Image.open('images/numbers/y0.4.png')
    IMAGE_ARRAY = numpy.asarray(IMAGE)
    print(IMAGE_ARRAY)
    pyplot.imshow(IMAGE_ARRAY)
    pyplot.show()
