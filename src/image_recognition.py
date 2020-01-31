"""
DOCSTRING
"""
from collections import Counter
from statistics import mean
from PIL import Image
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

if __name__ == '__main__':
    what_number_is_this('images/numbers/3.1.png')
