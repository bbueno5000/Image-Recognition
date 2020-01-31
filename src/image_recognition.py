"""
DOCSTRING
"""
from collections import Counter
from statistics import mean
from matplotlib import style
from matplotlib import pyplot
import numpy
from PIL import Image

style.use("ggplot")

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

def what_number_is_this(filepath):
    """
    DOCSTRING
    """
    matched_array = []
    load_examples = open('data/number_array_examples.txt', 'r').read()
    load_examples = load_examples.split('\n')
    image = Image.open(filepath)
    image_array = numpy.array(image)
    image_array_list = image_array.tolist()
    in_question = str(image_array_list)
    for each_example in load_examples:
        try:
            split_example = each_example.split('::')
            current_number = split_example[0]
            current_array = split_example[1]
            each_pixel_in_example = current_array.split('],')
            each_pixel_in_question = in_question.split('],')
            x_variable = 0
            while x_variable < len(each_pixel_in_example):
                if each_pixel_in_example[x_variable] == each_pixel_in_question[x_variable]:
                    matched_array.append(int(current_number))
                x_variable += 1
        except Exception as exception:
            print(str(exception))
    print(matched_array)
    x_variable = Counter(matched_array)
    print(x_variable)
    print(x_variable[0])
    graph_x = []
    graph_y = []
    for each_thing in x_variable:
        graph_x.append(each_thing)
        graph_y.append(x_variable[each_thing])
    axis_1 = pyplot.subplot2grid((4, 4), (0, 0), rowspan=1, colspan=4)
    axis_2 = pyplot.subplot2grid((4, 4), (1, 0), rowspan=3, colspan=4)
    axis_1.imshow(image_array)
    axis_2.bar(graph_x, graph_y, align='center')
    pyplot.ylim(400)
    x_location = pyplot.MaxNLocator(12)
    axis_2.xaxis.set_major_locator(x_location)
    pyplot.show()

if __name__ == '__main__':
    what_number_is_this('images/numbers/3.1.png')
