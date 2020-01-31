"""
DOCSTRING
"""
from statistics import mean
from PIL import Image
import matplotlib.pyplot as pyplot
import numpy

def create_examples():
    """
    DOCSTRING
    """
    number_array_examples = open('number_array_examples.txt', 'a')
    numbers_we_have = range(1, 10)
    for each_number in numbers_we_have:
        for further_number in numbers_we_have:
            print(str(each_number) + '.' + str(further_number))
            image_filepath = (
                'images/numbers/'
                + str(each_number)
                + '.'
                + str(further_number)
                + '.png'
                )
            example_image = Image.open(image_filepath)
            example_image_array = numpy.array(example_image)
            example_image_array_list = str(example_image_array.tolist())
            print(example_image_array_list)
            line_to_write = str(each_number) + '::' + example_image_array_list + '\n'
            number_array_examples.write(line_to_write)

def threshold(image_array):
    """
    DOCSTRING
    """
    balance_array = []
    new_array = image_array
    for each_row in image_array:
        for each_pixel in each_row:
            average = mean(each_pixel[:3])
            balance_array.append(average)
    balance = mean(balance_array)
    for each_row in new_array:
        for each_pixel in each_row:
            if mean(each_pixel[:3]) > balance:
                each_pixel[0] = 255
                each_pixel[1] = 255
                each_pixel[2] = 255
                each_pixel[3] = 255
            else:
                each_pixel[0] = 0
                each_pixel[1] = 0
                each_pixel[2] = 0
                each_pixel[3] = 255
    return new_array

if __name__ == '__main__':
    #IMAGE_1 = Image.open('images/numbers/0.1.png')
    #IMAGE_ARRAY_1 = numpy.array(IMAGE_1)
    #IMAGE_2 = Image.open('images/numbers/y0.4.png')
    #IMAGE_ARRAY_2 = numpy.array(IMAGE_2)
    #IMAGE_3 = Image.open('images/numbers/y0.5.png')
    #IMAGE_ARRAY_3 = numpy.array(IMAGE_3)
    #IMAGE_4 = Image.open('images/sentdex.png')
    #IMAGE_ARRAY_4 = numpy.array(IMAGE_4)
    #IMAGE_ARRAY_1 = threshold(IMAGE_ARRAY_1)
    #IMAGE_ARRAY_2 = threshold(IMAGE_ARRAY_2)
    #IMAGE_ARRAY_3 = threshold(IMAGE_ARRAY_3)
    #IMAGE_ARRAY_4 = threshold(IMAGE_ARRAY_4)
    #FIGURE = pyplot.figure()
    #AXIS_1 = pyplot.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
    #AXIS_2 = pyplot.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
    #AXIS_3 = pyplot.subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
    #AXIS_4 = pyplot.subplot2grid((8, 6), (4, 3), rowspan=4, colspan=3)
    #AXIS_1.imshow(IMAGE_ARRAY_1)
    #AXIS_2.imshow(IMAGE_ARRAY_2)
    #AXIS_3.imshow(IMAGE_ARRAY_3)
    #AXIS_4.imshow(IMAGE_ARRAY_4)
    #pyplot.show()
    create_examples()